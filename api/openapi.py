import json
from enum import Enum, StrEnum
from typing import Any, NotRequired, TypedDict

from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.responses import Response
from fastapi.routing import APIRoute

from api.constants import VERSION
from api.logging import get_logger, log_errors
from api.settings import Environment, Settings
from api.utils.authorization import get_all_scopes

logger = get_logger(__name__)


class OpenAPIExternalDoc(TypedDict):
    pass  # TODO: implement


class OpenAPITag(TypedDict):
    pass  # TODO: implement


class APITag(StrEnum):
    pass  # TODO: implement





    def metadata(cls) -> list[OpenAPITag]:
        pass  # TODO: implement


def generate_operation_id(route: APIRoute) -> str:
    pass  # TODO: implement


class OpenAPIParameters(TypedDict):
    pass  # TODO: implement


def get_openapi_parameters(settings: Settings) -> OpenAPIParameters:
    pass  # TODO: implement


OPENAPI_URL = "/openapi.json"


# This is required to keep same format on live endpoint and the dumped openapi schema
def dump_openapi(schema: dict[str, Any]) -> str:
    pass  # TODO: implement


def set_openapi_route(app: FastAPI) -> None:
    pass  # TODO: implement



def set_openapi_generator(app: FastAPI, settings: Settings) -> None:
    pass  # TODO: implement
    def _openapi_generator() -> dict[str, Any]:
        pass  # TODO: implement





__all__ = [
]
