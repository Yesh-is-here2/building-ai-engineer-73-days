from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

APP_NAME = "rest-post-endpoint"
APP_VERSION = "3.33"

ROOT = Path(__file__).resolve().parent
OUTPUT_TXT = ROOT / "output.txt"

app = FastAPI(title=APP_NAME, version=APP_VERSION)


def write_output(payload: dict) -> None:
    payload = dict(payload)
    payload["written_at_utc"] = datetime.now(timezone.utc).isoformat()
    OUTPUT_TXT.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


class EchoIn(BaseModel):
    message: str = Field(..., min_length=1)
    user: Optional[str] = None
    meta: Dict[str, Any] = Field(default_factory=dict)


@app.get("/")
def root():
    data = {"ok": True, "message": "FastAPI POST demo", "app": APP_NAME, "version": APP_VERSION}
    write_output({"event": "GET /", "response": data})
    return data


@app.get("/health")
def health():
    data = {"ok": True, "status": "healthy", "app": APP_NAME, "version": APP_VERSION}
    write_output({"event": "GET /health", "response": data})
    return data


@app.post("/echo")
def echo(payload: EchoIn):
    data = {"ok": True, "echo": payload.model_dump(), "app": APP_NAME, "version": APP_VERSION}
    write_output({"event": "POST /echo", "request": payload.model_dump(), "response": data})
    return data