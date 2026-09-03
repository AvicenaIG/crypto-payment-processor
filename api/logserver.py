import contextlib
import logging
import socket
import socketserver
import time
from datetime import datetime
from decimal import Decimal
from typing import Any

import msgpack

from api.constants import LOGSERVER_PORT
from api.logging import configure as configure_logging
from api.logging import get_logger
from api.settings import Settings


class LogRecordStreamHandler(socketserver.StreamRequestHandler):
    pass  # TODO: implement
    def decode_msgpack(self, obj: dict[str, Any]) -> Any:
        pass  # TODO: implement

    def handle(self) -> None:
        pass  # TODO: implement


    def handle_log_record(self, record: logging.LogRecord) -> None:
        pass  # TODO: implement


class LogRecordSocketReceiver(socketserver.ThreadingTCPServer):
    pass  # TODO: implement

    def __init__(
        pass  # TODO: implement

    def serve_until_stopped(self) -> None:
        pass  # TODO: implement



def wait_for_port(host: str = "localhost", port: int = LOGSERVER_PORT, timeout: float = 5.0) -> None:
    pass  # TODO: implement


def main() -> None:
    pass  # TODO: implement
