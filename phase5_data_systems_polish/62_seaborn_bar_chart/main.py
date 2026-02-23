from pathlib import Path
import json
import time
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

ART_DIR = Path("artifacts/files")
PLOT_PATH = ART_DIR / "bar_chart.png"
METRICS_PATH = ART_DIR / "bar_metrics.json"

def main():

    t0 = time.time()

    ART_DIR.mkdir(parents=True, exist_ok=True)

    # deterministic offline dataset
    categories = ["Model_A", "Model_B", "Model_C", "Model_D"]
    accuracy = [0.78, 0.83, 0.81, 0.88]

    plt.figure()

    sns.barplot(
        x=categories,
        y=accuracy
    )

    plt.title("Day 62 - Seaborn Bar Chart (offline-safe)")
    plt.xlabel("Model")
    plt.ylabel("Accuracy")

    plt.tight_layout()

    plt.savefig(PLOT_PATH, dpi=160)

    plt.close()

    metrics = {

        "bars": len(categories),

        "max_accuracy": max(accuracy),

        "min_accuracy": min(accuracy),

        "plot_file": str(PLOT_PATH).replace("\\\\","/"),

        "elapsed_seconds":
        round(time.time()-t0,6)

    }

    METRICS_PATH.write_text(
        json.dumps(metrics,indent=2),
        encoding="utf-8"
    )

    print("Bar chart generated.")
    print(f"PNG: {PLOT_PATH}")
    print(f"Metrics: {METRICS_PATH}")
    print(f"Bars: {metrics['bars']} | Elapsed: {metrics['elapsed_seconds']}s")


if __name__ == "__main__":
    main()
