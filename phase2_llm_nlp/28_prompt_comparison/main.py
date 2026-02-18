import os
from datetime import datetime

PHASE = "PHASE 2.28 - Prompt Comparison"
HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "output.txt")


def fake_llm(prompt: str) -> str:
    """
    Offline stand-in to demonstrate why prompt wording matters.
    Keeps this module runnable without API keys.
    """
    p = prompt.lower()

    if "json" in p and "schema" in p:
        return (
            '{"task":"summarize_phase2","style":"structured","bullets":['
            '"2.19 embeddings","2.20 faiss search","2.21 chroma store/retrieve"'
            '],"risk":"no-api"}'
        )

    if "step-by-step" in p or "steps" in p:
        return (
            "1) Read the input.\n"
            "2) Extract key points.\n"
            "3) Organize them into ordered steps.\n"
            "4) Output with short, numbered instructions."
        )

    if "one sentence" in p:
        return "Phase 2 so far built embeddings + similarity search and basic vector store retrieval."

    # default: vague prompt -> vague response
    return "We worked on a few NLP/LLM modules and made progress."


def main():
    ts = datetime.now().isoformat(timespec="seconds")
    cmd = r"python phase2_llm_nlp\28_prompt_comparison\main.py"

    base_task = "Summarize what we built in Phase 2 so far (19–21)."

    prompts = [
        ("Prompt A (vague)", base_task),
        ("Prompt B (one sentence)", base_task + " Respond in ONE sentence."),
        ("Prompt C (step-by-step)", base_task + " Provide step-by-step bullet points."),
        ("Prompt D (strict JSON)", base_task + " Output STRICT JSON following this schema: {task, style, bullets, risk}."),
    ]

    lines = []
    lines.append(f"{PHASE}")
    lines.append(f"Date: {ts}")
    lines.append(f"Command: {cmd}")
    lines.append("")
    lines.append("Goal:")
    lines.append(base_task)
    lines.append("")
    lines.append("Results (offline stub, demonstrates prompt effect):")
    lines.append("")

    for title, p in prompts:
        out = fake_llm(p)
        lines.append(f"{title}:")
        lines.append(f"Prompt: {p}")
        lines.append("Output:")
        lines.append(out)
        lines.append("-" * 60)

    lines.append("")
    lines.append("Notes:")
    lines.append("- More constraints => more predictable outputs (format, length, structure).")
    lines.append("- This module stays runnable offline; later we can swap fake_llm() with a real API call.")

    text = "\n".join(lines) + "\n"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)

    print(text)


if __name__ == "__main__":
    main()
