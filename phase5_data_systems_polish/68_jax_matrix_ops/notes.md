Day 68 - JAX Matrix Ops (offline-safe)

Goal:
- Demonstrate core matrix operations used in ML systems:
  - matrix multiply (A@B)
  - matrix-vector multiply (A@v)
  - transpose (B.T)
  - reduction (sum)

Implementation:
- Uses JAX if installed (shows backend: cpu/gpu/tpu)
- Falls back to NumPy if JAX is not available

Artifacts:
- artifacts/files/matrix_results.json
- artifacts/files/matrix_metrics.json
- artifacts/files/main_output.txt

Why JAX matters:
- JAX supports vectorization and accelerator execution (GPU/TPU).
- Similar workflow to modern ML compute graphs: define math, run fast backend.
