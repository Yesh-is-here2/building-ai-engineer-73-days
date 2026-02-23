import json
import time
from pathlib import Path

ART_DIR = Path("artifacts/files")
TOPIC_FILE = ART_DIR / "topic_messages.jsonl"
CONSUMED_FILE = ART_DIR / "consumed_messages.json"
METRICS_FILE = ART_DIR / "kafka_metrics.json"

def producer():

    messages = []

    for i in range(1, 11):
        msg = {
            "event_id": i,
            "event_type": "prediction_request",
            "value": i * 10,
            "timestamp": time.time()
        }
        messages.append(msg)

    return messages


def publish(messages):

    ART_DIR.mkdir(parents=True, exist_ok=True)

    with TOPIC_FILE.open("w", encoding="utf-8") as f:
        for m in messages:
            f.write(json.dumps(m) + "\n")


def consume():

    consumed = []

    with TOPIC_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            consumed.append(json.loads(line))

    return consumed


def main():

    t0 = time.time()

    ART_DIR.mkdir(parents=True, exist_ok=True)

    # Producer
    messages = producer()

    # Publish
    publish(messages)

    # Consumer
    consumed = consume()

    CONSUMED_FILE.write_text(
        json.dumps(consumed, indent=2),
        encoding="utf-8"
    )

    metrics = {
        "messages_produced": len(messages),
        "messages_consumed": len(consumed),
        "topic_file": str(TOPIC_FILE),
        "elapsed_seconds": round(time.time()-t0,6),
        "note": "Offline Kafka-style pub/sub simulation"
    }

    METRICS_FILE.write_text(
        json.dumps(metrics, indent=2),
        encoding="utf-8"
    )

    print("Kafka simulation complete.")
    print(f"Topic: {TOPIC_FILE}")
    print(f"Consumed: {CONSUMED_FILE}")
    print(f"Metrics: {METRICS_FILE}")
    print(f"Messages={metrics['messages_produced']} | Elapsed={metrics['elapsed_seconds']}s")


if __name__ == "__main__":
    main()
