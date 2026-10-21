import sys, random, csv, pathlib
from PIL import Image, ImageDraw
src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
files = sorted(src.rglob("*.jpg"))
cells = {}
for f in files:
    m, p, r, n = f.stem.split("_")
    cells.setdefault((m, p, r), []).append(f)
keys = sorted(cells); random.Random(20261021).shuffle(keys)
roles = {"R1":"Zhuge Liang","R2":"Guan Yu","R3":"Yang Yuhuan","R4":"Mu Guiying","R5":"Bao Zheng","R6":"Zhao Yun","R7":"Su San","R8":"Jiang Gan"}
with open(out/"key_DO_NOT_OPEN.csv","w",newline="") as fk:
    w = csv.writer(fk); w.writerow(["sheet","model","strategy","role","rep","file"])
    for i, k in enumerate(keys, 1):
        sid = f"S{i:02d}"
        ims = [Image.open(f).convert("RGB") for f in sorted(cells[k])]
        H = 600; ims = [im.resize((int(im.width*H/im.height), H)) for im in ims]
        W = sum(im.width for im in ims) + 10*(len(ims)-1)
        sheet = Image.new("RGB", (W, H+40), "white"); x = 0
        d = ImageDraw.Draw(sheet)
        for j, (im, f) in enumerate(zip(ims, sorted(cells[k])), 1):
            sheet.paste(im, (x, 40)); d.text((x+5, 10), f"{sid}-{j}  {k[2]} {roles[k[2]]}", fill="black")
            w.writerow([sid, k[0], k[1], k[2], j, f.name]); x += im.width + 10
        sheet.save(out/f"{sid}_{k[2]}.jpg", quality=85)
print(len(keys), "sheets")
