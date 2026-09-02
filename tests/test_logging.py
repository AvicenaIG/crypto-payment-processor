import logging
import time
from collections.abc import Iterator, Mapping

import pytest
import structlog
from opentelemetry import trace
from opentelemetry._logs import LogRecord, set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk._logs.export import InMemoryLogRecordExporter, SimpleLogRecordProcessor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.util.types import AnyValue

from api.logging import Logger, get_exception_details, get_exception_summary, get_logger
from api.logging import configure as configure_logging
from api.settings import Settings


@pytest.fixture(scope="session")
def otel_exporter() -> InMemoryLogRecordExporter:
    pass  # TODO: implement


@pytest.fixture
def exported(settings: Settings, otel_exporter: InMemoryLogRecordExporter) -> Iterator[InMemoryLogRecordExporter]:
    pass  # TODO: implement


@pytest.fixture
def logger(request: pytest.FixtureRequest, exported: InMemoryLogRecordExporter) -> Logger:
    pass  # TODO: implement


def only_record(exported: InMemoryLogRecordExporter) -> LogRecord:
    pass  # TODO: implement


def only_scope(exported: InMemoryLogRecordExporter) -> str:
    pass  # TODO: implement


def only_attributes(exported: InMemoryLogRecordExporter) -> Mapping[str, AnyValue]:
    pass  # TODO: implement


def test_structlog_record_is_exported_once(exported: InMemoryLogRecordExporter, logger: Logger) -> None:
    pass  # TODO: implement


def test_stdlib_record_is_exported_once(exported: InMemoryLogRecordExporter) -> None:
    pass  # TODO: implement


def test_stdlib_record_goes_through_structlog(exported: InMemoryLogRecordExporter) -> None:
    pass  # TODO: implement


def test_scope_is_the_logger_name(exported: InMemoryLogRecordExporter) -> None:
    pass  # TODO: implement


def test_trace_id_is_set_on_the_record(exported: InMemoryLogRecordExporter, logger: Logger) -> None:
    pass  # TODO: implement


def test_service_name_is_not_an_attribute(exported: InMemoryLogRecordExporter, logger: Logger) -> None:
    pass  # TODO: implement


def test_exception_is_exported(exported: InMemoryLogRecordExporter, logger: Logger) -> None:
    pass  # TODO: implement


@pytest.fixture
def named_timezone(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    pass  # TODO: implement


def test_timestamp_is_event_time(exported: InMemoryLogRecordExporter, logger: Logger, named_timezone: None) -> None:
    pass  # TODO: implement


def test_reconfiguring_keeps_app_loggers_enabled(settings: Settings) -> None:
    pass  # TODO: implement


@pytest.mark.parametrize(
)
def test_exception_summary(exc: Exception, expected: str) -> None:
    pass  # TODO: implement


def test_exception_details() -> None:
    pass  # TODO: implement
