from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from pathlib import Path

import redis

ROOT = Path(__file__).resolve().parent
OUTPUT_TXT = ROOT / "output.txt"
ERRORS_TXT = ROOT / "artifacts" / "logs" / "errors.txt"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_output(payload: dict) -> None:
    payload = dict(payload)
    payload["written_at_utc"] = utc_now()
    OUTPUT_TXT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def append_error(msg: str) -> None:
    ERRORS_TXT.parent.mkdir(parents=True, exist_ok=True)
    ERRORS_TXT.write_text("", encoding="utf-8") if not ERRORS_TXT.exists() else None
    with ERRORS_TXT.open("a", encoding="utf-8") as f:
        f.write(msg.rstrip() + "\n")


def main() -> int:
    payload = {
        "module": "3.35",
        "redis": {"host": "127.0.0.1", "port": 6379, "db": 0},
        "steps": [],
        "ok": False,
    }

    key = "phase3.35:hello"
    value = f"cached at {utc_now()}"

    try:
        r = redis.Redis(host="127.0.0.1", port=6379, db=0, socket_connect_timeout=1)
        t0 = time.time()
        pong = r.ping()
        payload["steps"].append({"action": "PING", "result": pong, "ms": round((time.time() - t0) * 1000, 2)})

        t1 = time.time()
        r.set(key, value, ex=60)
        payload["steps"].append({"action": "SET", "key": key, "value": value, "ttl_sec": 60, "ms": round((time.time() - t1) * 1000, 2)})

        t2 = time.time()
        got = r.get(key)
        got_s = got.decode("utf-8") if got else None
        payload["steps"].append({"action": "GET", "key": key, "value": got_s, "ms": round((time.time() - t2) * 1000, 2)})

        payload["ok"] = (got_s == value)
        payload["note"] = "Success: Redis reachable and GET matched SET value." if payload["ok"] else "Redis reachable but GET did not match."
        write_output(payload)
        return 0

    except Exception as e:
        payload["ok"] = False
        payload["note"] = "Redis not reachable. This is expected if Redis server is not installed/running on Windows."
        payload["error"] = {"type": type(e).__name__, "message": str(e)}
        write_output(payload)

        append_error(
            f"[{utc_now()}] Redis connection failed: {type(e).__name__}: {e}"
        )
        return 0


if __name__ == "__main__":
    raise SystemExit(main())