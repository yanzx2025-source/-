"""Figure 3: example images. Usage: python fig3_montage.py <p1 folder> <folder with 768px jpgs>"""
import sys, pathlib, pandas as pd
from PIL import Image, ImageDraw, ImageFont
P, IMG = sys.argv[1], pathlib.Path(sys.argv[2])
key = pd.read_csv(f"{P}/data/sheet_key.csv"); key["img"] = key.sheet + "-" + key.rep.astype(str)
picks = [("S06-1", "(a) Compliant: Bao Zheng, black python robe, minister's hat, crescent"),
         ("S02-1", "(b) Zhuge Liang in a python robe and official's hat, no fan"),
         ("S09-1", "(c) Su San in a lake-blue xuezi, jewelled headdress, no cangue"),
         ("S01-3", "(d) Su San with a Qing court headdress (cross-cultural)"),
         ("S30-1", "(e) 'Pleated robe': literal knife pleats for xuezi"),
         ("S39-1", "(f) 'Fish-shaped cangue': square board carved with a fish")]
files = {r.img: r.file for r in key.itertuples()}
font = ImageFont.truetype("DejaVuSans.ttf", 24)
tiles = []
for img, cap in picks:
    f = next(IMG.rglob(files[img]))
    im = Image.open(f).convert("RGB"); im.thumbnail((768, 768))
    t = Image.new("RGB", (788, 860), "white"); t.paste(im, ((788 - im.width) // 2, 10))
    d = ImageDraw.Draw(t); m = next(r for r in key.itertuples() if r.img == img)
    name = {"deepseek": "Hunyuan", "doubao": "Doubao", "muse": "Meta AI"}[m.model]
    words, lines, line = (cap + f" [{name}, {m.strategy}]").split(), [], ""
    for w in words:
        if d.textlength(line + " " + w, font=font) > 760: lines.append(line); line = w
        else: line = (line + " " + w).strip()
    lines.append(line)
    for i, l in enumerate(lines[:3]): d.text((10, 790 + i * 26 - (len(lines) - 2) * 13), l, fill="#1f1f1e", font=font)
    tiles.append(t)
W, H = 3 * 788, 2 * 860
out = Image.new("RGB", (W, H), "white")
for i, t in enumerate(tiles): out.paste(t, ((i % 3) * 788, (i // 3) * 860))
out.save(f"{P}/figures/fig3_examples.png", dpi=(300, 300))
print("ok")
