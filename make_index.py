from pathlib import Path

# ✅ change this to your repo
REPO_URL = "https://github.com/Yesh-is-here2/building-ai-engineer-73-days/tree/main"

REPO = Path(".").resolve()
OUT_DIR = REPO / "phase5_data_systems_polish" / "72_portfolio_index"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "index.html"

PHASES = [
    ("Phase 1 — Core ML", "phase1_core_ml"),
    ("Phase 2 — LLM / NLP", "phase2_llm_nlp"),
    ("Phase 3 — Software AI", "phase3_software_ai"),
    ("Phase 4 — MLOps / Cloud", "phase4_mlops_cloud"),
    ("Phase 5 — Data Systems / Polish", "phase5_data_systems_polish"),
]

def list_modules(phase_dir: Path):
    return sorted([p for p in phase_dir.iterdir() if p.is_dir()])

rows = []

for title, folder in PHASES:
    phase_dir = REPO / folder
    rows.append(f"<h2>{title}</h2><ul>")

    for m in list_modules(phase_dir):
        gh_link = f"{REPO_URL}/{folder}/{m.name}"
        rows.append(f"<li><a href='{gh_link}' target='_blank'><b>{m.name}</b></a></li>")

    rows.append("</ul>")

html = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>AI Engineer Portfolio Index</title>
<style>
body {{ font-family: Arial; margin: 40px; }}
h1 {{ margin-bottom: 6px; }}
h2 {{ margin-top: 28px; }}
li {{ margin-bottom: 8px; }}
a {{ text-decoration: none; color: #1a0dab; }}
a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
<h1>AI Engineer Portfolio Index</h1>
<div>Yeshwanth Akula — Artifact-based proof of work (73-day build)</div>
{''.join(rows)}
</body>
</html>
"""

OUT.write_text(html, encoding="utf-8")
print("Wrote:", OUT)