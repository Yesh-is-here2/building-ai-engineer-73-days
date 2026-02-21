from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI

APP_NAME = "fastapi-hello"
APP_VERSION = "3.32"

ROOT = Path(__file__).resolve().parent
OUTPUT_TXT = ROOT / "output.txt"

app = FastAPI(title=APP_NAME, version=APP_VERSION)


def write_output(payload: dict) -> None:
    """
    Writes/overwrites module-root output.txt with a single JSON payload.
    This is the proof artifact for the module run.
    """
    payload = dict(payload)
    payload["written_at_utc"] = datetime.now(timezone.utc).isoformat()

    OUTPUT_TXT.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


@app.get("/")
def root():
    data = {"ok": True, "message": "Hello from FastAPI", "app": APP_NAME, "version": APP_VERSION}
    # Write proof output for the module whenever endpoint is hit
    write_output({"event": "GET /", "response": data})
    return data


@app.get("/health")
def health():
    data = {"ok": True, "status": "healthy", "app": APP_NAME, "version": APP_VERSION}
    write_output({"event": "GET /health", "response": data})
    return data