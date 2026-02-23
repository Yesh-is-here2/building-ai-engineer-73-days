Day 58 - Batch Inference

Goal:
- Simulate a production-style batch inference job (offline-safe).
- Read an input dataset (CSV), run a scoring function, and write predictions.

What this demo produces:
- artifacts/files/input.csv          (synthetic input if missing)
- artifacts/files/predictions.csv    (batch outputs)
- artifacts/files/metrics.json       (throughput + score stats)
- artifacts/files/main_output.txt    (execution proof)

Why batch inference matters:
- Used for nightly scoring, backfills, scheduled jobs, and large offline predictions.
- More cost-efficient than real-time inference for large volumes.
