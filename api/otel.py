import os

from opentelemetry.instrumentation import auto_instrumentation

from api.version import VERSION

# asyncpg spans duplicate the ones sqlalchemy instrumentation emits,
# structlog records are exported by api.logging.StructlogOTELProcessor instead
DISABLED_INSTRUMENTATIONS = ["asyncpg", "structlog"]


def append_resource_attributes() -> None:
    pass  # TODO: implement


def disable_instrumentations() -> None:
    pass  # TODO: implement


def initialize() -> None:
    pass  # TODO: implement
