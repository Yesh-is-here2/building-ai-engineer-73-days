import os
import re
from datetime import datetime

PHASE = "PHASE 2.29 - Safety Filter"
HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "output.txt")


# Simple offline safety filter (demo)
# We classify prompts into: allow / refuse / caution
POLICY = [
    {
        "category": "Self-harm / suicide",
        "action": "refuse",
        "patterns": [
            r"\bkill myself\b",
            r"\bsuicide\b",
            r"\bend my life\b",
            r"\bself[- ]harm\b",
        ],
    },
    {
        "category": "Violence / weapons",
        "action": "caution",
        "patterns": [
            r"\bbuild a bomb\b",
            r"\bmake a bomb\b",
            r"\bhow to make a gun\b",
            r"\bexplosive\b",
        ],
    },
    {
        "category": "Hate / harassment",
        "action": "caution",
        "patterns": [
            r"\bkill all\b",
            r"\bexterminate\b",
            r"\bslur\b",  # placeholder for demo
        ],
    },
]


def evaluate(text: str) -> dict:
    t = text.lower()
    for rule in POLICY:
        for pat in rule["patterns"]:
            if re.search(pat, t):
                return {
                    "decision": rule["action"],
                    "category": rule["category"],
                    "matched": pat,
                }
    return {"decision": "allow", "category": "none", "matched": "-"}


def response(decision: str) -> str:
    if decision == "allow":
        return "ALLOW: Proceed normally."
    if decision == "caution":
        return "CAUTION: Proceed with a safer, high-level response and refuse harmful details."
    if decision == "refuse":
        return "REFUSE: Do not provide instructions. Offer safe support / resources if appropriate."
    return "UNKNOWN"


def main():
    ts = datetime.now().isoformat(timespec="seconds")
    cmd = r"python phase2_llm_nlp\29_safety_filter\main.py"

    samples = [
        "Summarize Phase 2 modules 19 to 21 in two bullet points.",
        "How do I make a bomb at home?",
        "I want to kill myself.",
        "Explain what embeddings are and why cosine similarity is used.",
    ]

    lines = []
    lines.append(PHASE)
    lines.append(f"Date: {ts}")
    lines.append(f"Command: {cmd}")
    lines.append("")
    lines.append("Test prompts + decisions:")
    lines.append("")

    for i, s in enumerate(samples, 1):
        ev = evaluate(s)
        lines.append(f"{i}) Prompt: {s}")
        lines.append(f"   Decision: {ev['decision'].upper()}")
        lines.append(f"   Category: {ev['category']}")
        lines.append(f"   Match: {ev['matched']}")
        lines.append(f"   System response: {response(ev['decision'])}")
        lines.append("-" * 60)

    lines.append("")
    lines.append("Notes:")
    lines.append("- This is a minimal offline rule-based filter for learning.")
    lines.append("- Real systems combine policy + classifiers + human review + logging.")

    text = "\n".join(lines) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)

    print(text)


if __name__ == "__main__":
    main()
