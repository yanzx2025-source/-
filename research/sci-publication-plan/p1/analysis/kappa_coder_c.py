"""Agreement of human coder C with coder A, coder B and the consensus on the 48-image subset.
Usage: python kappa_coder_c.py <coder C xlsx>"""
import sys
import pandas as pd
from pathlib import Path

P = Path(__file__).resolve().parents[1] / 'data'
D = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']

def kappa(x, y):
    cats = sorted(set(x) | set(y)); n = len(x)
    po = sum(a == b for a, b in zip(x, y)) / n
    pe = sum((list(x).count(c) / n) * (list(y).count(c) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe < 1 else float('nan'), po

c = pd.read_excel(sys.argv[1]).iloc[:, [0] + list(range(4, 10))]
c.columns = ['hid'] + D
key = pd.read_csv(P / 'coder_C_key.csv')
a = pd.read_csv(P / 'coder_A_author_codes.csv').iloc[:, [0] + list(range(2, 8))]; a.columns = ['img'] + D
b = pd.read_csv(P / 'coder_B_model_codes_blind.csv')[['img'] + D]
s = pd.read_csv(P / 'consensus_codes.csv')[['img'] + D]
c = c.merge(key[['hid', 'img']], on='hid')
assert len(c) == 48 and c[D].isin([0, 1, 9]).all().all(), 'missing or invalid codes'
for name, ref in (('C vs A', a), ('C vs B', b), ('C vs consensus', s)):
    m = c.merge(ref, on='img', suffixes=('_c', '_r'))
    xs, ys = [], []
    row = [name]
    for d in D:
        k, po = kappa(m[d + '_c'], m[d + '_r']); row.append(f'{k:.2f}')
        xs += list(m[d + '_c']); ys += list(m[d + '_r'])
    k, po = kappa(xs, ys)
    print(' | '.join(row + [f'overall κ {k:.2f}, agreement {po:.1%}']))
