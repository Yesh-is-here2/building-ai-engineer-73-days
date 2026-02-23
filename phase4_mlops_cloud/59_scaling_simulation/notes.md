Day 59 - Scaling Simulation

Goal:
- Demonstrate horizontal scaling behavior using a simple worker/job scheduling simulation.

What this demo does:
- Creates a deterministic set of job durations.
- Schedules jobs onto N workers using a greedy load-balancing strategy.
- Computes scaling metrics:
  - makespan (wall time)
  - speedup (T1 / TN)
  - efficiency (speedup / N)

Artifacts produced:
- artifacts/files/main_output.txt
- artifacts/files/results.csv
- artifacts/files/results.json

What to look for:
- Increasing workers reduces makespan, but speedup shows diminishing returns.
- Efficiency drops as workers increase due to load imbalance / overhead effects (simulated by varied job sizes).
