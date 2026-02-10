# Tiny 'repro' example: reproduce mean/variance from a fixed seed.
import numpy as np

rng = np.random.default_rng(0)
x = rng.normal(size=1000)

print("mean:", float(x.mean()))
print("var :", float(x.var()))
