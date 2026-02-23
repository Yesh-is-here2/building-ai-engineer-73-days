import json
import time
from dataclasses import dataclass
from pathlib import Path
from statistics import mean

ART_DIR = Path("artifacts/files")
RESULTS_CSV = ART_DIR / "results.csv"
RESULTS_JSON = ART_DIR / "results.json"

# -----------------------------
# Scaling simulation (offline-safe)
# -----------------------------
# Idea:
# - We simulate N jobs with known durations (seconds).
# - We assign jobs to W workers using a simple greedy scheduler:
#   always send next job to the currently-least-busy worker.
# - Then we compute:
#   - makespan (total wall time) for W workers
#   - speedup = T1 / TW
#   - efficiency = speedup / W
#
# This models horizontal scaling: more workers => less total time,
# but with diminishing returns when overhead/imbalance exists.

@dataclass
class RunResult:
    workers: int
    jobs: int
    makespan_s: float
    avg_worker_load_s: float
    max_worker_load_s: float
    speedup: float
    efficiency: float

def build_jobs(n: int = 50) -> list[float]:
    # deterministic job durations (no randomness)
    # mix of short/medium/long jobs to show imbalance effects
    durations = []
    for i in range(1, n + 1):
        base = (i % 10) * 0.02  # 0..0.18
        extra = 0.05 if (i % 7 == 0) else 0.0
        durations.append(0.03 + base + extra)  # ~0.03..0.26
    return durations

def greedy_schedule(job_durations: list[float], workers: int) -> list[float]:
    # worker_loads[w] = total assigned time
    worker_loads = [0.0] * workers
    for d in job_durations:
        # choose least-loaded worker
        idx = min(range(workers), key=lambda i: worker_loads[i])
        worker_loads[idx] += d
    return worker_loads

def simulate(job_durations: list[float], workers: int) -> float:
    # We compute makespan from loads. (No actual sleeping needed.)
    loads = greedy_schedule(job_durations, workers)
    return max(loads)

def run_all(job_count: int = 50, worker_options: list[int] = None) -> tuple[list[RunResult], dict]:
    if worker_options is None:
        worker_options = [1, 2, 3, 4, 6, 8]

    jobs = build_jobs(job_count)

    t1 = simulate(jobs, 1)
    results: list[RunResult] = []

    for w in worker_options:
        loads = greedy_schedule(jobs, w)
        makespan = max(loads)
        avg_load = mean(loads)
        speedup = (t1 / makespan) if makespan > 0 else 0.0
        efficiency = (speedup / w) if w > 0 else 0.0

        results.append(
            RunResult(
                workers=w,
                jobs=len(jobs),
                makespan_s=round(makespan, 6),
                avg_worker_load_s=round(avg_load, 6),
                max_worker_load_s=round(max(loads), 6),
                speedup=round(speedup, 6),
                efficiency=round(efficiency, 6),
            )
        )

    summary = {
        "jobs": len(jobs),
        "total_work_s": round(sum(jobs), 6),
        "t1_makespan_s": round(t1, 6),
        "worker_options": worker_options,
        "note": "Makespan is computed from scheduled worker loads (offline-safe).",
    }
    return results, summary

def write_csv(results: list[RunResult], path: Path) -> None:
    header = "workers,jobs,makespan_s,speedup,efficiency,avg_worker_load_s,max_worker_load_s\n"
    lines = [header]
    for r in results:
        lines.append(
            f"{r.workers},{r.jobs},{r.makespan_s},{r.speedup},{r.efficiency},{r.avg_worker_load_s},{r.max_worker_load_s}\n"
        )
    path.write_text("".join(lines), encoding="utf-8")

def main():
    ART_DIR.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    results, summary = run_all(job_count=50, worker_options=[1, 2, 3, 4, 6, 8])
    elapsed = time.time() - t0

    write_csv(results, RESULTS_CSV)
    payload = {
        "summary": summary,
        "results": [r.__dict__ for r in results],
        "script_elapsed_s": round(elapsed, 6),
    }
    RESULTS_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print("Scaling simulation complete.")
    print(f"Jobs: {summary['jobs']} | Total work (s): {summary['total_work_s']}")
    print(f"Artifacts: {RESULTS_CSV} , {RESULTS_JSON}")
    print("Table (workers -> makespan_s, speedup, efficiency):")
    for r in results:
        print(f"  {r.workers:>2} -> {r.makespan_s:>8} s | {r.speedup:>7}x | eff={r.efficiency}")

if __name__ == "__main__":
    main()
