"""Batch image generation for the xiqu costume audit (Gemini API, no extra packages).

    export GEMINI_API_KEY=...
    python3 generate_gemini.py --model gemini-2.5-flash-image --n 3 --strategies P1,P2
Re-running skips files that already exist.
"""
import argparse, base64, csv, datetime, json, pathlib, time, urllib.error, urllib.request, os

from prompts import prompt_for

URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"


def generate(model, prompt, key):
    body = json.dumps({"contents": [{"parts": [{"text": prompt}]}],
                       "generationConfig": {"responseModalities": ["IMAGE"]}}).encode()
    req = urllib.request.Request(URL.format(model=model), data=body,
                                 headers={"Content-Type": "application/json", "x-goog-api-key": key})
    with urllib.request.urlopen(req, timeout=180) as r:
        data = json.load(r)
    for part in data["candidates"][0]["content"]["parts"]:
        if "inlineData" in part:
            return base64.b64decode(part["inlineData"]["data"])
    raise RuntimeError("no image in response: " + json.dumps(data)[:300])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="gemini-2.5-flash-image")
    ap.add_argument("--n", type=int, default=3)
    ap.add_argument("--strategies", default="P1,P2")
    ap.add_argument("--out", default="images")
    ap.add_argument("--pause", type=float, default=6.0, help="seconds between calls (free-tier rate limit)")
    args = ap.parse_args()

    key = os.environ["GEMINI_API_KEY"]
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
            for strategy in args.strategies.split(","):
                prompt = prompt_for(r, strategy)
                for rep in range(1, args.n + 1):
                    name = f"{args.model}_{strategy}_{r['id']}_{rep}.png"
                    path = out / name
                    if path.exists():
                        continue
                    try:
                        path.write_bytes(generate(args.model, prompt, key))
                        status = "ok"
                    except urllib.error.HTTPError as e:
                        status = f"error {e.code}: {e.read()[:200]!r}"
                    except Exception as e:
                        status = f"error: {e}"
                    log.writerow([name, args.model, strategy, r["id"], rep, prompt,
                                  datetime.datetime.utcnow().isoformat(timespec="seconds"), status])
                    f.flush()
                    print(name, status)
                    time.sleep(args.pause)


if __name__ == "__main__":
    main()
