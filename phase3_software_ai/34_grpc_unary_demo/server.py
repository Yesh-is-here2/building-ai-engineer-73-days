from __future__ import annotations

from concurrent import futures
from datetime import datetime, timezone

import grpc

import hello_pb2
import hello_pb2_grpc


class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        now = datetime.now(timezone.utc).isoformat()
        msg = f"Hello, {request.name}! (utc={now})"
        return hello_pb2.HelloReply(message=msg)


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("127.0.0.1:50051")
    server.start()
    print("grpc server listening on 127.0.0.1:50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()