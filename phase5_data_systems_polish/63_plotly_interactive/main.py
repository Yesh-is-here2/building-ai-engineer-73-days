from pathlib import Path
import json
import time
import plotly.graph_objects as go

ART_DIR = Path("artifacts/files")

HTML_PATH = ART_DIR / "interactive_plot.html"
METRICS_PATH = ART_DIR / "plot_metrics.json"

def main():

    t0 = time.time()

    ART_DIR.mkdir(parents=True, exist_ok=True)

    # deterministic dataset
    x = list(range(1, 21))

    y1 = [i*1.5 for i in x]
    y2 = [i*1.1+2 for i in x]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y1,
            mode="lines+markers",
            name="Series_A"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y2,
            mode="lines+markers",
            name="Series_B"
        )
    )

    fig.update_layout(
        title="Day 63 - Plotly Interactive Chart",
        xaxis_title="X",
        yaxis_title="Y"
    )

    fig.write_html(HTML_PATH)

    metrics = {

        "points": len(x),

        "html_file": str(HTML_PATH).replace("\\\\","/"),

        "elapsed_seconds":
        round(time.time()-t0,6)

    }

    METRICS_PATH.write_text(
        json.dumps(metrics,indent=2),
        encoding="utf-8"
    )

    print("Interactive plot generated.")
    print(f"HTML: {HTML_PATH}")
    print(f"Metrics: {METRICS_PATH}")
    print(f"Points: {metrics['points']} | Elapsed: {metrics['elapsed_seconds']}s")


if __name__ == "__main__":
    main()

