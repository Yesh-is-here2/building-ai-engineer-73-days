import json
import time
from pathlib import Path

ART_DIR = Path("artifacts/files")
RESULTS_JSON = ART_DIR / "matrix_results.json"
METRICS_JSON = ART_DIR / "matrix_metrics.json"

def main():
    t0 = time.time()
    ART_DIR.mkdir(parents=True, exist_ok=True)

    backend = "unknown"

    # Small deterministic matrices
    A_list = [
        [1.0, 2.0, 3.0],
        [0.0, 1.0, 4.0],
        [5.0, 6.0, 0.0],
    ]
    B_list = [
        [2.0, 0.0, 1.0],
        [1.0, 3.0, 2.0],
        [0.0, 1.0, 1.0],
    ]
    v_list = [1.0, 2.0, 3.0]

    try:
        import jax
        import jax.numpy as jnp

        backend = f"jax ({jax.default_backend()})"

        A = jnp.array(A_list)
        B = jnp.array(B_list)
        v = jnp.array(v_list)

        C = A @ B              # matmul
        Av = A @ v             # matvec
        Bt = B.T               # transpose
        s = jnp.sum(C)         # reduction

        # Convert to python lists for JSON serialization
        results = {
            "A": A.tolist(),
            "B": B.tolist(),
            "C=A@B": C.tolist(),
            "A@v": Av.tolist(),
            "B_T": Bt.tolist(),
            "sum(C)": float(s),
        }

    except Exception:
        # Offline-safe fallback (no JAX required)
        import numpy as np

        backend = "numpy (fallback)"

        A = np.array(A_list, dtype=float)
        B = np.array(B_list, dtype=float)
        v = np.array(v_list, dtype=float)

        C = A @ B
        Av = A @ v
        Bt = B.T
        s = float(C.sum())

        results = {
            "A": A.tolist(),
            "B": B.tolist(),
            "C=A@B": C.tolist(),
            "A@v": Av.tolist(),
            "B_T": Bt.tolist(),
            "sum(C)": s,
        }

    RESULTS_JSON.write_text(json.dumps(results, indent=2), encoding="utf-8")

    metrics = {
        "backend": backend,
        "elapsed_seconds": round(time.time() - t0, 6),
        "note": "Matrix ops demo: matmul, transpose, reduction. Uses JAX if installed, else NumPy fallback."
    }
    METRICS_JSON.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    print("Matrix ops complete.")
    print(f"Backend: {backend}")
    print(f"Results: {RESULTS_JSON}")
    print(f"Metrics: {METRICS_JSON}")
    print(f"Elapsed: {metrics['elapsed_seconds']}s")

if __name__ == "__main__":
    main()
