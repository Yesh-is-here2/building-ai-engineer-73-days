from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple


ROOT = Path(__file__).resolve().parent
OUTPUT_TXT = ROOT / "output.txt"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_output(payload: Dict[str, Any]) -> None:
    payload = dict(payload)
    payload["written_at_utc"] = utc_now()
    OUTPUT_TXT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


@dataclass(frozen=True)
class Request:
    user: str
    action: str
    amount: float
    currency: str
    source: str  # e.g., "api", "ui", "job"
    request_id: str


def log(step_logs: List[Dict[str, Any]], step: str, **fields: Any) -> None:
    entry = {"step": step, **fields, "at_utc": utc_now()}
    step_logs.append(entry)


def validate(req: Request) -> Tuple[bool, List[str]]:
    errors: List[str] = []
    if not req.user.strip():
        errors.append("user is required")
    if req.action not in {"charge", "refund"}:
        errors.append("action must be 'charge' or 'refund'")
    if req.amount <= 0:
        errors.append("amount must be > 0")
    if req.currency not in {"USD", "EUR", "INR"}:
        errors.append("unsupported currency")
    if req.source not in {"api", "ui", "job"}:
        errors.append("invalid source")
    if not req.request_id.strip():
        errors.append("request_id is required")
    return (len(errors) == 0, errors)


def normalize(req: Request) -> Request:
    # Example “business rule” normalization
    user = req.user.strip().lower()
    action = req.action.strip().lower()
    currency = req.currency.strip().upper()
    source = req.source.strip().lower()
    return Request(
        user=user,
        action=action,
        amount=float(req.amount),
        currency=currency,
        source=source,
        request_id=req.request_id.strip(),
    )


def risk_score(req: Request) -> float:
    # Very simple deterministic scoring (demo)
    score = 0.0
    if req.amount >= 500:
        score += 0.6
    if req.source == "api":
        score += 0.2
    if req.action == "refund":
        score += 0.2
    return min(score, 1.0)


def decide(req: Request) -> Dict[str, Any]:
    score = risk_score(req)
    decision = "approve" if score < 0.7 else "manual_review"
    return {"decision": decision, "risk_score": round(score, 2)}


def main() -> int:
    logs: List[Dict[str, Any]] = []

    # Demo inputs (2 cases)
    requests = [
        Request(user="Yesh", action="charge", amount=49.99, currency="usd", source="ui", request_id="req-001"),
        Request(user="Yesh", action="refund", amount=999.00, currency="usd", source="api", request_id="req-002"),
    ]

    results: List[Dict[str, Any]] = []

    for req in requests:
        log(logs, "RECEIVED", request=req.__dict__)

        norm = normalize(req)
        log(logs, "NORMALIZED", request=norm.__dict__)

        ok, errs = validate(norm)
        log(logs, "VALIDATED", ok=ok, errors=errs)

        if not ok:
            results.append({"request_id": norm.request_id, "status": "rejected", "errors": errs})
            log(logs, "DONE", status="rejected")
            continue

        decision = decide(norm)
        log(logs, "DECIDED", **decision)

        results.append({"request_id": norm.request_id, "status": decision["decision"], "risk_score": decision["risk_score"]})
        log(logs, "DONE", status=decision["decision"])

    payload = {
        "module": "3.37",
        "ok": True,
        "results": results,
        "log_count": len(logs),
        "logs": logs,
    }
    write_output(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())