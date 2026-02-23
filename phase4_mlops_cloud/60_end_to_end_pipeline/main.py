import csv
import json
import math
import time
from pathlib import Path
from statistics import mean

ART_DIR = Path("artifacts/files")
DATA_CSV = ART_DIR / "data.csv"
MODEL_JSON = ART_DIR / "model.json"
METRICS_JSON = ART_DIR / "metrics.json"
PRED_CSV = ART_DIR / "predictions.csv"
SUMMARY_TXT = ART_DIR / "pipeline_summary.txt"

# -----------------------------
# Stage 1: Data ingest (deterministic synthetic regression data)
# y = 3.0*x1 - 2.0*x2 + 1.5 + small deterministic noise
# -----------------------------
def ensure_data(path: Path, n: int = 120) -> None:
    if path.exists():
        return
    ART_DIR.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "x1", "x2", "y"])
        for i in range(1, n + 1):
            x1 = (i % 20) * 0.35
            x2 = (i % 15) * 0.25
            noise = ((i % 7) - 3) * 0.05  # deterministic "noise"
            y = 3.0 * x1 - 2.0 * x2 + 1.5 + noise
            w.writerow([i, f"{x1:.6f}", f"{x2:.6f}", f"{y:.6f}"])

# -----------------------------
# Stage 2: Train (simple linear regression via gradient descent)
# Model: y_hat = w1*x1 + w2*x2 + b
# -----------------------------
def load_rows(path: Path) -> list[tuple[float, float, float]]:
    rows = []
    with path.open("r", newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            x1 = float(row["x1"])
            x2 = float(row["x2"])
            y = float(row["y"])
            rows.append((x1, x2, y))
    return rows

def train_gd(rows: list[tuple[float, float, float]], lr: float = 0.08, epochs: int = 600) -> dict:
    w1, w2, b = 0.0, 0.0, 0.0
    n = len(rows)

    for _ in range(epochs):
        dw1 = dw2 = db = 0.0
        for x1, x2, y in rows:
            yhat = w1 * x1 + w2 * x2 + b
            err = (yhat - y)
            dw1 += err * x1
            dw2 += err * x2
            db  += err

        # mean gradients (MSE derivative factor 2 is absorbed into lr here)
        dw1 /= n
        dw2 /= n
        db  /= n

        w1 -= lr * dw1
        w2 -= lr * dw2
        b  -= lr * db

    return {"w1": w1, "w2": w2, "b": b, "lr": lr, "epochs": epochs}

# -----------------------------
# Stage 3: Evaluate
# -----------------------------
def predict(model: dict, x1: float, x2: float) -> float:
    return model["w1"] * x1 + model["w2"] * x2 + model["b"]

def eval_metrics(rows: list[tuple[float, float, float]], model: dict) -> dict:
    errs = []
    sqerrs = []
    for x1, x2, y in rows:
        yhat = predict(model, x1, x2)
        e = yhat - y
        errs.append(abs(e))
        sqerrs.append(e * e)

    mae = mean(errs) if errs else None
    rmse = math.sqrt(mean(sqerrs)) if sqerrs else None
    return {"mae": mae, "rmse": rmse}

# -----------------------------
# Stage 4: Batch predictions artifact
# -----------------------------
def write_predictions(rows: list[tuple[float, float, float]], model: dict, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["row", "x1", "x2", "y_true", "y_pred", "abs_error"])
        for i, (x1, x2, y) in enumerate(rows, start=1):
            yhat = predict(model, x1, x2)
            w.writerow([i, f"{x1:.6f}", f"{x2:.6f}", f"{y:.6f}", f"{yhat:.6f}", f"{abs(yhat-y):.6f}"])

def main():
    t0 = time.time()
    ART_DIR.mkdir(parents=True, exist_ok=True)

    # 1) ingest
    ensure_data(DATA_CSV, n=120)
    rows = load_rows(DATA_CSV)

    # split train/eval (deterministic)
    split = int(0.8 * len(rows))
    train_rows = rows[:split]
    eval_rows = rows[split:]

    # 2) train
    model = train_gd(train_rows, lr=0.08, epochs=600)
    MODEL_JSON.write_text(json.dumps(model, indent=2), encoding="utf-8")

    # 3) evaluate
    m = eval_metrics(eval_rows, model)
    metrics = {
        "train_rows": len(train_rows),
        "eval_rows": len(eval_rows),
        "mae": round(m["mae"], 6) if m["mae"] is not None else None,
        "rmse": round(m["rmse"], 6) if m["rmse"] is not None else None,
        "elapsed_seconds": round(time.time() - t0, 6),
    }
    METRICS_JSON.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    # 4) predictions
    write_predictions(eval_rows, model, PRED_CSV)

    # 5) summary
    summary = f"""Day 60 - End-to-End Pipeline (Offline-Safe)

Stages:
1) Ingest: generated/used {DATA_CSV}
2) Train:  trained linear model -> {MODEL_JSON}
3) Eval:   metrics -> {METRICS_JSON}
4) Predict: batch predictions -> {PRED_CSV}

Key results:
- train_rows = {metrics['train_rows']}
- eval_rows  = {metrics['eval_rows']}
- mae        = {metrics['mae']}
- rmse       = {metrics['rmse']}
- elapsed_s  = {metrics['elapsed_seconds']}

Notes:
- No cloud dependencies. No external services.
- Artifacts are committed so GitHub shows proof of execution.
"""
    SUMMARY_TXT.write_text(summary, encoding="utf-8")

    print("End-to-end pipeline complete.")
    print(f"Data:      {DATA_CSV}")
    print(f"Model:     {MODEL_JSON}")
    print(f"Metrics:   {METRICS_JSON}")
    print(f"Preds:     {PRED_CSV}")
    print(f"Summary:   {SUMMARY_TXT}")
    print(f"MAE={metrics['mae']} | RMSE={metrics['rmse']} | Elapsed={metrics['elapsed_seconds']}s")

if __name__ == "__main__":
    main()
