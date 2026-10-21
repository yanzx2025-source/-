"""Sensitivity analyses for the main GEE model (strategy and channel odds ratios)."""
import sys, numpy as np, pandas as pd, statsmodels.api as sm, statsmodels.formula.api as smf
data = sys.argv[1]  # folder with consensus_codes.csv, coder_A_author_codes.csv, coder_B_model_codes_blind.csv, sheet_key.csv
D = ["D1", "D2", "D3", "D4", "D5", "D6"]
key = pd.read_csv(f"{data}/sheet_key.csv"); key["img"] = key.sheet + "-" + key.rep.astype(str)

def long(codes, na_as_compliant=False):
    c = codes[["img"] + D].merge(key[["img", "model", "strategy", "role"]], on="img")
    l = c.melt(id_vars=["img", "model", "strategy", "role"], value_vars=D, var_name="dim", value_name="v")
    if na_as_compliant: l.loc[l.v == 9, "v"] = 0
    l = l[l.v != 9].copy(); l["y"] = l.v.astype(int); return l

def fit(l, label):
    m = smf.gee("y ~ C(strategy) + C(model) + C(dim) + C(role)", groups="img", data=l,
                family=sm.families.Binomial(), cov_struct=sm.cov_struct.Exchangeable()).fit()
    ci = m.conf_int()
    out = {k: f"{np.exp(m.params[k]):.3f} ({np.exp(ci.loc[k,0]):.3f}-{np.exp(ci.loc[k,1]):.3f})"
           for k in m.params.index if "strategy" in k or "model" in k}
    print(f"{label:<38} n={len(l):<4}", out)

cons = pd.read_csv(f"{data}/consensus_codes.csv")
a = pd.read_csv(f"{data}/coder_A_author_codes.csv"); a.columns = ["img", "role_", *D, "rec", "note"]
b = pd.read_csv(f"{data}/coder_B_model_codes_blind.csv")
fit(long(cons), "main (consensus)")
fit(long(cons)[lambda x: x.img != "S34-2"], "excluding watermark image S34-2")
fit(long(cons, na_as_compliant=True), "NA counted as compliant")
fit(long(cons)[lambda x: x.dim != "D3"], "excluding D3 (motif)")
fit(long(cons)[lambda x: x.dim != "D1"], "excluding D1 (garment type)")
fit(long(a), "coder A only (before adjudication)")
fit(long(b), "coder B only")
