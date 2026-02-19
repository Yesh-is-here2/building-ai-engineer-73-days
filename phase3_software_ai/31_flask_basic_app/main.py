from __future__ import annotations

from datetime import datetime
from pathlib import Path
import platform
import textwrap

# Flask app
from flask import Flask, jsonify

MODULE = "PHASE 3.31 - Flask Basic App"
ROOT = Path(__file__).resolve().parent
OUTPUT_PATH = ROOT / "output.txt"

app = Flask(__name__)

@app.get("/")
def home():
    return "OK: Flask app is running"

@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "flask-basic-app"})


def write_output():
    now = datetime.now().isoformat(timespec="seconds")
    cmd = r"python phase3_software_ai\31_flask_basic_app\main.py"

    content = f"""{MODULE}
Date: {now}
Command: {cmd}
Python: {platform.python_version()}
Platform: {platform.platform()}

What this module proves:
- Minimal Flask API with two routes:
  GET /       -> plain text
  GET /health -> JSON status

How to run:
1) python phase3_software_ai\\31_flask_basic_app\\main.py
2) In another terminal:
   curl http://127.0.0.1:5000/
   curl http://127.0.0.1:5000/health

Notes:
- This file writes this output.txt, then starts the Flask dev server.
"""
    OUTPUT_PATH.write_text(textwrap.dedent(content), encoding="utf-8")


if __name__ == "__main__":
    write_output()
    print(OUTPUT_PATH.read_text(encoding="utf-8"))
    # Start dev server
    app.run(host="127.0.0.1", port=5000, debug=False)