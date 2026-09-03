import logging
import re
import traceback
import uuid
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import datetime
from decimal import Decimal
from logging.handlers import TimedRotatingFileHandler
from typing import Any, TypeVar, cast

import msgpack
import structlog
from opentelemetry import trace
from opentelemetry._logs import LogRecord, NoOpLogger
from opentelemetry.instrumentation.structlog import StructlogProcessor
from structlog.dev import plain_traceback

from api.constants import LOGSERVER_PORT
from api.schemas.base import Schema
from api.settings import Settings

RendererType = TypeVar("RendererType")

Logger = structlog.stdlib.BoundLogger

TIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f %Z"

app_loggers: set[str] = set()


class MsgpackHandler(logging.handlers.SocketHandler):
    pass  # TODO: implement
    def __init__(self, host: str, port: int) -> None:
        pass  # TODO: implement

    def msgpack_encoder(self, obj: Any) -> Any:
        pass  # TODO: implement

    def makePickle(self, record: logging.LogRecord) -> bytes:
        pass  # TODO: implement


class StructlogOTELProcessor(StructlogProcessor):
    pass  # TODO: implement
    def __call__(self, logger: Any, method_name: str, event_dict: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO: implement

    def _translate(self, event_dict: dict[str, Any], method_name: str | None = None) -> LogRecord:
        pass  # TODO: implement


class FormattingNullHandler(logging.Handler):
    pass  # TODO: implement
    def emit(self, record: logging.LogRecord) -> None:
        pass  # TODO: implement


class Logging[RendererType]:
    pass  # TODO: implement




    def get_level(cls, settings: Settings) -> str:
        pass  # TODO: implement

    def is_debug(cls, settings: Settings) -> bool:
        pass  # TODO: implement

    def debug_loggers(cls, settings: Settings) -> list[str]:
        pass  # TODO: implement

    def add_trace_context(cls, logger: Logger, method_name: str, event_dict: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO: implement

    def remove_callsite_params(
        pass  # TODO: implement

    def get_common_processors(cls, *, settings: Settings) -> list[Any]:
        pass  # TODO: implement

    def get_structlog_processors(cls, *, settings: Settings) -> list[Any]:
        pass  # TODO: implement

    def get_renderer(cls) -> RendererType:
        pass  # TODO: implement

    def get_file_renderer(cls) -> RendererType:
        pass  # TODO: implement

    def get_third_party_loggers(cls, settings: Settings) -> list[str]:
        pass  # TODO: implement

    def get_custom_level(cls, level: str, module: str) -> str | int:
        pass  # TODO: implement

    def configure_third_party() -> None:
        pass  # TODO: implement

    def maybe_add_otel_handler(
        pass  # TODO: implement

    def configure_stdlib(cls, *, settings: Settings, logserver: bool = False) -> None:
        pass  # TODO: implement

    def configure_structlog(cls, *, settings: Settings) -> None:
        pass  # TODO: implement

    def configure(cls, *, settings: Settings, logserver: bool = False) -> None:
        pass  # TODO: implement

    def timed_log_namer(default_name: str) -> str:
        pass  # TODO: implement

    def configure_file_logging(
        pass  # TODO: implement


class Development(Logging[structlog.dev.ConsoleRenderer]):
    pass  # TODO: implement
    def get_renderer(cls) -> structlog.dev.ConsoleRenderer:
        pass  # TODO: implement

    def get_file_renderer(cls) -> structlog.dev.ConsoleRenderer:
        pass  # TODO: implement


# TODO: implement it one day

# class Production(Logging[structlog.processors.JSONRenderer]):
#     @classmethod
#     def get_renderer(cls) -> structlog.processors.JSONRenderer:
#         return structlog.processors.JSONRenderer()

#     @classmethod
#     def get_file_renderer(cls) -> structlog.processors.JSONRenderer:
#         return structlog.processors.JSONRenderer()

Production = Development


def configure(*, settings: Settings, logserver: bool = False) -> None:
    pass  # TODO: implement


def generate_correlation_id() -> str:
    pass  # TODO: implement


def get_exception_message(exc: Exception) -> str:
    pass  # TODO: implement


def get_exception_summary(exc: BaseException) -> str:
    pass  # TODO: implement


def get_exception_details(exc: BaseException) -> str:
    pass  # TODO: implement


@contextmanager
def log_errors(logger: Logger) -> Iterator[None]:  # pragma: no cover
    pass  # TODO: implement


def get_logger(name: str) -> Logger:
    pass  # TODO: implement
