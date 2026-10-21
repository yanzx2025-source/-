import sys, pandas as pd, numpy as np
import statsmodels.api as sm, statsmodels.formula.api as smf
S = sys.argv[1]
c = pd.read_csv(f"{S}/codes_B.csv")
k = pd.read_csv(f"{S}/sheets/key_DO_NOT_OPEN.csv"); k["img"] = k.sheet + "-" + k.rep.astype(str)
d = c.merge(k, on="img"); assert len(d) == 144
D = ["D1","D2","D3","D4","D5","D6"]
long = d.melt(id_vars=["img","model","strategy","role"], value_vars=D, var_name="dim", value_name="v")
long = long[long.v != 9].copy()
d["n_viol"] = (d[D] == 1).sum(1); d["n_obs"] = (d[D] != 9).sum(1); d["any"] = (d.n_viol > 0).astype(int)
d["fully_compliant"] = 1 - d["any"]
pd.set_option("display.width", 200)
print("== violation rate by model x strategy (share of coded items)")
print(long.groupby(["model","strategy"]).v.mean().unstack().round(3))
print("== share of images fully compliant")
print(d.groupby(["model","strategy"]).fully_compliant.mean().unstack().round(3))
print("== violation rate by dimension x strategy")
print(long.groupby(["dim","strategy"]).v.mean().unstack().round(3))
print("== violation rate by role x strategy")
print(long.groupby(["role","strategy"]).v.mean().unstack().round(3))
print("== mean violations per image by model x strategy")
print(d.groupby(["model","strategy"]).n_viol.mean().unstack().round(2))
# item-level logistic GEE, clustered by image
long["y"] = long.v.astype(int)
m = smf.gee("y ~ C(strategy) * C(model) + C(dim) + C(role)", groups="img", data=long, family=sm.families.Binomial(), cov_struct=sm.cov_struct.Exchangeable()).fit()
print(m.summary().tables[1])
m2 = smf.gee("y ~ C(strategy) + C(model) + C(dim) + C(role)", groups="img", data=long, family=sm.families.Binomial(), cov_struct=sm.cov_struct.Exchangeable()).fit()
print("== main-effects model, odds ratios")
print(pd.DataFrame({"OR": np.exp(m2.params), "lo": np.exp(m2.conf_int()[0]), "hi": np.exp(m2.conf_int()[1]), "p": m2.pvalues}).round(3))
d.to_csv(f"{S}/coded_unblinded.csv", index=False); long.to_csv(f"{S}/coded_long.csv", index=False)
