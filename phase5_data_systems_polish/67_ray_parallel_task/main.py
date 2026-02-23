import json
import time
from multiprocessing import Pool
from pathlib import Path

ART_DIR = Path("artifacts/files")
RESULTS_FILE = ART_DIR / "parallel_results.json"
METRICS_FILE = ART_DIR / "parallel_metrics.json"

# Simulated "remote task"
def process_task(x):

    # pretend computation
    time.sleep(0.05)

    return {
        "input": x,
        "result": x * x
    }


def main():

    t0 = time.time()

    ART_DIR.mkdir(parents=True, exist_ok=True)

    tasks = list(range(1, 11))

    # Parallel execution
    with Pool(4) as p:
        results = p.map(process_task, tasks)

    RESULTS_FILE.write_text(
        json.dumps(results, indent=2),
        encoding="utf-8"
    )

    metrics = {
        "tasks": len(tasks),
        "workers": 4,
        "elapsed_seconds": round(time.time()-t0,6),
        "note": "Ray-style parallel task simulation"
    }

    METRICS_FILE.write_text(
        json.dumps(metrics, indent=2),
        encoding="utf-8"
    )

    print("Parallel tasks complete.")
    print(f"Results: {RESULTS_FILE}")
    print(f"Metrics: {METRICS_FILE}")
    print(f"Tasks={metrics['tasks']} | Workers={metrics['workers']} | Elapsed={metrics['elapsed_seconds']}s")


if __name__ == "__main__":
    main()
