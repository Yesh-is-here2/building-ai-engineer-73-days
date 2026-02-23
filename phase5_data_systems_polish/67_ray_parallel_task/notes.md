Day 67 - Ray Parallel Tasks (offline-safe)

Goal:
- Simulate Ray-style distributed task execution.

Pipeline:

Tasks -> Workers -> Results

Artifacts:

- artifacts/files/parallel_results.json
- artifacts/files/parallel_metrics.json
- artifacts/files/main_output.txt

Why this matters:

- Ray is used for distributed ML workloads.
- Parallel training and batch inference use this pattern.
