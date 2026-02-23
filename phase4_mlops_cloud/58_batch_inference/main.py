import csv
import json
import time
from pathlib import Path
from statistics import mean

ART_DIR = Path("artifacts/files")
INPUT_CSV = ART_DIR / "input.csv"
OUTPUT_CSV = ART_DIR / "predictions.csv"
METRICS_JSON = ART_DIR / "metrics.json"

def ensure_input_csv(path: Path, n: int = 50) -> None:
    # Create a tiny synthetic dataset if input is missing
    # Columns: id, x1, x2
    if path.exists():
        return
    ART_DIR.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "x1", "x2"])
        for i in range(1, n + 1):
            # simple deterministic numbers (no randomness) for reproducibility
            x1 = (i % 10) * 0.7
            x2 = (i % 7) * 1.3
            w.writerow([i, x1, x2])

def model_score(x1: float, x2: float) -> float:
    # Offline-safe "model": a tiny scoring function
    # score = sigmoid-ish mapping without needing numpy
    z = 0.9 * x1 - 0.4 * x2 + 0.2
    # fast bounded transform
    return 1.0 / (1.0 + (2.718281828 ** (-z)))

def run_batch(input_path: Path, output_path: Path) -> dict:
    t0 = time.time()

    rows = []
    scores = []

    with input_path.open("r", newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            _id = int(row["id"])
            x1 = float(row["x1"])
            x2 = float(row["x2"])
            score = model_score(x1, x2)
            pred = 1 if score >= 0.5 else 0
            rows.append((_id, x1, x2, score, pred))
            scores.append(score)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "x1", "x2", "score", "prediction"])
        for _id, x1, x2, score, pred in rows:
            w.writerow([_id, x1, x2, f"{score:.6f}", pred])

    dt = time.time() - t0
    metrics = {
        "input_rows": len(rows),
        "output_rows": len(rows),
        "avg_score": round(mean(scores), 6) if scores else None,
        "min_score": round(min(scores), 6) if scores else None,
        "max_score": round(max(scores), 6) if scores else None,
        "elapsed_seconds": round(dt, 6),
        "throughput_rows_per_sec": round((len(rows) / dt), 3) if dt > 0 else None,
    }
    return metrics

def main():
    ART_DIR.mkdir(parents=True, exist_ok=True)
    ensure_input_csv(INPUT_CSV, n=50)

    metrics = run_batch(INPUT_CSV, OUTPUT_CSV)
    METRICS_JSON.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    print("Batch inference complete.")
    print(f"Input:  {INPUT_CSV}")
    print(f"Output: {OUTPUT_CSV}")
    print(f"Metrics: {METRICS_JSON}")
    print(f"Rows: {metrics['input_rows']} | Elapsed: {metrics['elapsed_seconds']}s")

if __name__ == "__main__":
    main()
