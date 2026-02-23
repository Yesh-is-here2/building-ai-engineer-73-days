from pathlib import Path
import json
import time
import matplotlib
matplotlib.use("Agg")  # headless-safe (no UI needed)
import matplotlib.pyplot as plt

ART_DIR = Path("artifacts/files")
PLOT_PATH = ART_DIR / "line_plot.png"
METRICS_PATH = ART_DIR / "plot_metrics.json"

def main():
    t0 = time.time()
    ART_DIR.mkdir(parents=True, exist_ok=True)

    # deterministic data (no randomness)
    x = list(range(1, 21))
    y1 = [i * 1.2 for i in x]
    y2 = [i * 0.9 + 3 for i in x]

    plt.figure()
    plt.plot(x, y1, label="series_1")
    plt.plot(x, y2, label="series_2")
    plt.title("Day 61 - Matplotlib Line Plot (offline-safe)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.tight_layout()
    plt.savefig(PLOT_PATH, dpi=160)
    plt.close()

    metrics = {
        "points": len(x),
        "plot_file": str(PLOT_PATH).replace("\\\\", "/"),
        "elapsed_seconds": round(time.time() - t0, 6),
    }
    METRICS_PATH.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    print("Plot generated.")
    print(f"PNG: {PLOT_PATH}")
    print(f"Metrics: {METRICS_PATH}")
    print(f"Points: {metrics['points']} | Elapsed: {metrics['elapsed_seconds']}s")

if __name__ == "__main__":
    main()
