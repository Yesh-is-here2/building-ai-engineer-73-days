from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

from pymongo import MongoClient
from pymongo.errors import PyMongoError

ROOT = Path(__file__).resolve().parent
OUTPUT_TXT = ROOT / "output.txt"
ERRORS_TXT = ROOT / "artifacts" / "logs" / "errors.txt"

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://127.0.0.1:27017")
DB_NAME = "ai_engineer_73"
COLLECTION = "phase3_36_docs"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_output(payload: Dict[str, Any]) -> None:
    payload = dict(payload)
    payload["written_at_utc"] = utc_now()
    OUTPUT_TXT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def append_error(line: str) -> None:
    ERRORS_TXT.parent.mkdir(parents=True, exist_ok=True)
    with ERRORS_TXT.open("a", encoding="utf-8") as f:
        f.write(line.rstrip() + "\n")


def main() -> int:
    payload: Dict[str, Any] = {
        "module": "3.36",
        "mongo_uri": MONGO_URI,
        "db": DB_NAME,
        "collection": COLLECTION,
        "ok": False,
        "steps": [],
    }

    doc = {
        "module": "3.36",
        "name": "yesh",
        "message": "hello mongodb",
        "created_at_utc": utc_now(),
        "meta": {"os": "windows", "shell": "powershell"},
    }

    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=1500)

        # Force server selection now (throws if not reachable)
        client.admin.command("ping")
        payload["steps"].append({"action": "PING", "result": "ok"})

        col = client[DB_NAME][COLLECTION]

        ins = col.insert_one(doc)
        payload["steps"].append({"action": "INSERT_ONE", "inserted_id": str(ins.inserted_id)})

        fetched = col.find_one({"_id": ins.inserted_id})
        if fetched and "_id" in fetched:
            fetched["_id"] = str(fetched["_id"])

        payload["steps"].append({"action": "FIND_ONE", "document": fetched})

        payload["ok"] = fetched is not None
        payload["note"] = "Success: inserted and fetched document from MongoDB."
        write_output(payload)
        return 0

    except PyMongoError as e:
        payload["ok"] = False
        payload["note"] = "MongoDB not reachable. Expected if MongoDB server is not installed/running on Windows."
        payload["error"] = {"type": type(e).__name__, "message": str(e)}
        write_output(payload)
        append_error(f"[{utc_now()}] MongoDB connection/operation failed: {type(e).__name__}: {e}")
        return 0

    except Exception as e:
        payload["ok"] = False
        payload["note"] = "Unexpected error."
        payload["error"] = {"type": type(e).__name__, "message": str(e)}
        write_output(payload)
        append_error(f"[{utc_now()}] Unexpected error: {type(e).__name__}: {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())