"""Build the blind package for human coder C: one randomly chosen image per cell (48),
renamed H01-H48 in random order. The key stays in data/coder_C_key.csv."""
import sys, csv, random, shutil, pathlib
src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
P = pathlib.Path(__file__).resolve().parents[1]
key = list(csv.DictReader(open(P / 'data/sheet_key.csv')))
rng = random.Random(20261022)
cells = {}
for r in key:
    cells.setdefault((r['model'], r['strategy'], r['role']), []).append(r)
pick = [rng.choice(v) for _, v in sorted(cells.items())]
rng.shuffle(pick)
roles = {'R1': ('诸葛亮', '空城计'), 'R2': ('关羽', '单刀会'), 'R3': ('杨玉环', '贵妃醉酒'),
         'R4': ('穆桂英', '穆桂英挂帅'), 'R5': ('包拯', '铡美案'), 'R6': ('赵云', '长坂坡'),
         'R7': ('苏三', '玉堂春·起解'), 'R8': ('蒋干', '群英会')}
(out / 'images').mkdir(parents=True, exist_ok=True)
with open(P / 'data/coder_C_key.csv', 'w', newline='') as fk:
    w = csv.writer(fk); w.writerow(['hid', 'img', 'model', 'strategy', 'role', 'rep', 'file'])
    rows = []
    for i, r in enumerate(pick, 1):
        hid = f'H{i:02d}'
        f = next(src.rglob(r['file']))
        shutil.copy(f, out / 'images' / f'{hid}_{r["role"]}.jpg')
        w.writerow([hid, f"{r['sheet']}-{r['rep']}", r['model'], r['strategy'], r['role'], r['rep'], r['file']])
        rows.append((hid, r['role'], *roles[r['role']]))
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation
wb = Workbook(); ws = wb.active; ws.title = '编码'
ws.append(['编号', '角色ID', '角色', '剧目', 'D1形制', 'D2色彩', 'D3纹样', 'D4头戴', 'D5配件与标志', 'D6跨文化', '备注（可选）'])
for row in rows:
    ws.append(list(row))
dv = DataValidation(type='list', formula1='"0,1,9"', allow_blank=True); ws.add_data_validation(dv)
dv.add(f'E2:J{len(rows)+1}')
for c, wd in zip('ABCDEFGHIJK', [6, 7, 8, 13, 8, 8, 8, 8, 12, 9, 40]):
    ws.column_dimensions[c].width = wd
wb.save(out / '编码表_编码者C.xlsx')
print(len(rows), 'images')
