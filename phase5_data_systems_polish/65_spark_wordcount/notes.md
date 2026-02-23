Day 65 - Spark WordCount (offline-safe)

Goal:
- Demonstrate the classic Spark WordCount pipeline structure:
  read -> map -> shuffle/group -> reduce -> write results.

Why this matters:
- WordCount is the "hello world" of distributed data processing.
- The exact same logic is used in Spark jobs at scale; Spark just distributes it.

Artifacts produced:
- artifacts/files/wordcount_input.txt
- artifacts/files/wordcount_output.csv
- artifacts/files/wordcount_metrics.json
- artifacts/files/main_output.txt
