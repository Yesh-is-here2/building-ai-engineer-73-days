import csv
import json
import time
from pathlib import Path

ART_DIR = Path("artifacts/files")
DATA = ART_DIR / "sales_dashboard_data.csv"
META = ART_DIR / "dataset_meta.json"

def main():
    t0 = time.time()
    ART_DIR.mkdir(parents=True, exist_ok=True)

    # Deterministic synthetic sales dataset for dashboards (no randomness)
    # Columns: date, region, channel, product, orders, revenue, cost
    regions = ["Midwest", "South", "West", "Northeast"]
    channels = ["Online", "Retail", "Partner"]
    products = ["Starter", "Pro", "Enterprise"]

    rows = []
    # 90 days of data
    for day in range(1, 91):
        # fake date string (simple, dashboard-friendly)
        # (not using datetime to keep it ultra-simple)
        date = f"2026-01-{day:02d}" if day <= 31 else (f"2026-02-{day-31:02d}" if day <= 59 else f"2026-03-{day-59:02d}")

        for r_i, region in enumerate(regions, start=1):
            for c_i, channel in enumerate(channels, start=1):
                for p_i, product in enumerate(products, start=1):
                    base = (day % 10) + r_i + c_i + p_i
                    orders = 5 + (base * 2)
                    revenue = round(orders * (20 + p_i * 15) * (1 + 0.05 * c_i), 2)
                    cost = round(revenue * (0.55 + 0.03 * r_i), 2)
                    rows.append([date, region, channel, product, orders, revenue, cost])

    with DATA.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "region", "channel", "product", "orders", "revenue", "cost"])
        w.writerows(rows)

    meta = {
        "file": str(DATA).replace("\\\\", "/"),
        "rows": len(rows),
        "columns": ["date", "region", "channel", "product", "orders", "revenue", "cost"],
        "kpis_to_build": [
            "Total Revenue",
            "Total Orders",
            "Profit (Revenue - Cost)",
            "Profit Margin",
            "Revenue by Region",
            "Revenue by Channel",
            "Revenue Trend (Date)",
            "Top Products by Revenue"
        ],
        "elapsed_seconds": round(time.time() - t0, 6),
        "note": "Use this CSV in Power BI or Tableau to build a dashboard. Export screenshot/PDF as proof."
    }
    META.write_text(json.dumps(meta, indent=2), encoding="utf-8")

    print("Dashboard dataset generated.")
    print(f"CSV: {DATA}")
    print(f"Meta: {META}")
    print(f"Rows: {meta['rows']} | Elapsed: {meta['elapsed_seconds']}s")

if __name__ == "__main__":
    main()
