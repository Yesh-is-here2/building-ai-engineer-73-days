import json
import re
import time
from collections import Counter
from pathlib import Path

ART_DIR = Path("artifacts/files")
INPUT_TXT = ART_DIR / "wordcount_input.txt"
OUTPUT_CSV = ART_DIR / "wordcount_output.csv"
METRICS_JSON = ART_DIR / "wordcount_metrics.json"

def ensure_input(path: Path) -> None:
    if path.exists():
        return
    ART_DIR.mkdir(parents=True, exist_ok=True)

    text = """
Spark WordCount Demo (Offline-Safe)

This simulates Spark's classic wordcount pipeline:
1) Read text
2) Map: tokenize -> (word, 1)
3) Shuffle/GroupBy: group counts per word
4) Reduce: sum counts
5) Write results

Spark is used for big data, but the logic is the same even in pure Python.
We also include repeated terms: spark spark spark data data pipeline pipeline model model.
"""
    path.write_text(text.strip() + "\n", encoding="utf-8")

def tokenize(line: str) -> list[str]:
    # keep it deterministic and simple
    # words only, lowercase
    return re.findall(r"[a-zA-Z]+", line.lower())

def spark_like_wordcount(text: str) -> Counter:
    # "RDD" of lines
    lines = text.splitlines()

    # MAP: words -> (word, 1)
    pairs = []
    for line in lines:
        for w in tokenize(line):
            pairs.append((w, 1))

    # SHUFFLE/GROUP: group by word
    grouped = {}
    for w, one in pairs:
        grouped.setdefault(w, []).append(one)

    # REDUCE: sum
    counts = Counter()
    for w, ones in grouped.items():
        counts[w] = sum(ones)

    return counts

def write_csv(counts: Counter, path: Path, top_n: int = 30) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # top N by count desc, then word asc for stable ordering
    items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:top_n]

    lines = ["word,count\n"]
    for w, c in items:
        lines.append(f"{w},{c}\n")

    path.write_text("".join(lines), encoding="utf-8")

def main():
    t0 = time.time()
    ART_DIR.mkdir(parents=True, exist_ok=True)

    ensure_input(INPUT_TXT)
    text = INPUT_TXT.read_text(encoding="utf-8")

    counts = spark_like_wordcount(text)
    write_csv(counts, OUTPUT_CSV, top_n=30)

    metrics = {
        "input_file": str(INPUT_TXT).replace("\\\\", "/"),
        "output_file": str(OUTPUT_CSV).replace("\\\\", "/"),
        "unique_words": len(counts),
        "total_words": sum(counts.values()),
        "top_5": sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:5],
        "elapsed_seconds": round(time.time() - t0, 6),
        "note": "Offline-safe Spark-like WordCount (map/shuffle/reduce)."
    }
    METRICS_JSON.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    print("WordCount complete.")
    print(f"Input:   {INPUT_TXT}")
    print(f"Output:  {OUTPUT_CSV}")
    print(f"Metrics: {METRICS_JSON}")
    print(f"Total words={metrics['total_words']} | Unique={metrics['unique_words']} | Elapsed={metrics['elapsed_seconds']}s")

if __name__ == "__main__":
    main()
