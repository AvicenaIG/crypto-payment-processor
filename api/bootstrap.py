import asyncio
import contextlib
import sys
import traceback
from collections.abc import AsyncIterator, Awaitable, Callable
from typing import Any

from advanced_alchemy.exceptions import AdvancedAlchemyError, NotFoundError
from dishka.integrations.taskiq import setup_dishka as taskiq_setup_dishka
from fastapi import FastAPI, Request
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, PlainTextResponse
from scalar_fastapi import get_scalar_api_reference
from sqlalchemy.exc import IntegrityError
from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response
from starlette.staticfiles import StaticFiles
from starlette.types import Receive, Scope, Send

from api.db import AsyncSession
from api.exceptions import ExchangeRatesUnavailableError
from api.ext.agent import AgentError, AgentErrorCode
from api.ioc import build_container, setup_dishka
from api.ioc.services import ServicesProvider
from api.logging import configure as configure_logging
from api.logging import get_exception_details, get_logger
from api.middleware import LogCorrelationIdMiddleware, OnionHostMiddleware, PrometheusMiddleware
from api.openapi import generate_operation_id, get_openapi_parameters, set_openapi_generator, set_openapi_route
from api.sentry import configure_sentry
from api.services.host_agent import error_response
from api.services.plugin_registry import PluginRegistry
from api.settings import Settings
from api.tasks import broker, client_tasks_broker
from api.utils.common import excepthook_handler, handle_event_loop_exception
from api.views import router
from api.worker import start_broker_basic

logger = get_logger("api")


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:


# TODO: remove when https://github.com/AvicenaIG/fastapi/pull/11160 is merged
def patch_call(instance: FastAPI) -> None:
    pass  # TODO: implement
    class _(type(instance)):  # type: ignore[misc]
        pass  # TODO: implement



def with_db_rollback(
    pass  # TODO: implement
) -> Callable[[Request, Any], Awaitable[Response]]:





async def db_exception_handler(request: Request, exc: AdvancedAlchemyError) -> JSONResponse:


async def db_integrity_error_handler(request: Request, exc: IntegrityError) -> JSONResponse:


async def db_not_found_error_handler(request: Request, exc: NotFoundError) -> JSONResponse:


AGENT_ERROR_STATUSES: dict[str, int] = {
}


async def agent_error_handler(request: Request, exc: AgentError) -> JSONResponse:


async def exchange_rates_error_handler(request: Request, exc: ExchangeRatesUnavailableError) -> JSONResponse:


exception_handlers: dict[type[Exception], Callable[[Request, Any], Awaitable[Response]]] = {
}


def add_exception_handlers(app: FastAPI) -> None:
    pass  # TODO: implement



def get_app(settings: Settings) -> FastAPI:
    pass  # TODO: implement







def setup_prometheus(app: FastAPI, settings: Settings) -> None:
    pass  # TODO: implement



def configure_production_app() -> FastAPI:
    pass  # TODO: implement
