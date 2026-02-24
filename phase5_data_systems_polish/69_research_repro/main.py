import json
from pathlib import Path

import numpy as np

ART_DIR = Path("artifacts/files")
OUT_JSON = ART_DIR / "repro_metrics.json"

def run_experiment(seed: int = 42, n: int = 10_000) -> tuple[float, float]:
    """
    Deterministic experiment:
    - generate N samples from N(0,1) using a fixed seed
    - return mean and variance
    """
    rng = np.random.default_rng(seed)
    x = rng.normal(loc=0.0, scale=1.0, size=n)
    mean = float(x.mean())
    var = float(x.var())
    return mean, var

def main() -> None:
    ART_DIR.mkdir(parents=True, exist_ok=True)

    mean, var = run_experiment(seed=42, n=10_000)

    payload = {
        "seed": 42,
        "n": 10_000,
        "mean": mean,
        "var": var,
        "note": "Reproducibility demo: fixed seed -> identical results across runs."
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(f"mean: {mean}")
    print(f"var : {var}")
    print(f"wrote: {OUT_JSON}")

if __name__ == "__main__":
    main()
