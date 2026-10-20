"""Batch image generation for the xiqu costume audit (OpenAI Images API).

Run on your own computer:
    pip install openai
    export OPENAI_API_KEY=sk-...          # Windows: set OPENAI_API_KEY=sk-...
    python generate_openai.py --model gpt-image-1 --n 5
P3 needs one reference image per role at refs/R1.jpg ... refs/R8.jpg; roles without one are skipped.
Re-running skips files that already exist, so an interrupted run can resume.
"""
import argparse, base64, csv, datetime, json, pathlib
from openai import OpenAI

BASE = "A traditional Peking opera stage costume for {role} in the play {play}, {hangdang}. Full-body view of one performer, front-facing, plain light grey background, photographic realism."
STRUCT = " The costume must follow Peking opera dress codes: {spec}."


def prompt_for(r, strategy):
    p = BASE.format(**r)
    return p if strategy == "P1" else p + STRUCT.format(**r)


def save(b64, path):
    path.write_bytes(base64.b64decode(b64))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="gpt-image-1")
    ap.add_argument("--n", type=int, default=5)
    ap.add_argument("--size", default="1024x1024")
    ap.add_argument("--out", default="images")
    args = ap.parse_args()

    client = OpenAI()
    here = pathlib.Path(__file__).parent
    roles = json.loads((here / "roles.json").read_text(encoding="utf-8"))
    out = here / args.out
    out.mkdir(exist_ok=True)
    log_path = here / "generation_log.csv"
    new_log = not log_path.exists()
    with log_path.open("a", newline="", encoding="utf-8") as f:
        log = csv.writer(f)
        if new_log:
            log.writerow(["file", "model", "strategy", "role_id", "rep", "prompt", "timestamp_utc", "status"])
        for r in roles:
            for strategy in ("P1", "P2", "P3"):
                ref = here / "refs" / f"{r['id']}.jpg"
                if strategy == "P3" and not ref.exists():
                    continue
                prompt = prompt_for(r, strategy)
                for rep in range(1, args.n + 1):
                    name = f"{args.model}_{strategy}_{r['id']}_{rep}.png"
                    path = out / name
                    if path.exists():
                        continue
                    try:
                        if strategy == "P3":
                            with ref.open("rb") as img:
                                res = client.images.edit(model=args.model, image=img, prompt=prompt, size=args.size)
                        else:
                            res = client.images.generate(model=args.model, prompt=prompt, size=args.size, n=1)
                        save(res.data[0].b64_json, path)
                        status = "ok"
                    except Exception as e:  # keep going; failures are logged and retried on the next run
                        status = f"error: {e}"
                    log.writerow([name, args.model, strategy, r["id"], rep, prompt,
                                  datetime.datetime.utcnow().isoformat(timespec="seconds"), status])
                    f.flush()
                    print(name, status)


if __name__ == "__main__":
    main()
