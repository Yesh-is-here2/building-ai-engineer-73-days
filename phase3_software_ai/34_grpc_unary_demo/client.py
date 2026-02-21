from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import grpc

import hello_pb2
import hello_pb2_grpc

ROOT = Path(__file__).resolve().parent
OUTPUT_TXT = ROOT / "output.txt"


def main() -> None:
    name = "yesh"
    with grpc.insecure_channel("127.0.0.1:50051") as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        resp = stub.SayHello(hello_pb2.HelloRequest(name=name))

    payload = {
        "module": "3.34",
        "call": "Greeter.SayHello",
        "request": {"name": name},
        "response": {"message": resp.message},
        "written_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    OUTPUT_TXT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()