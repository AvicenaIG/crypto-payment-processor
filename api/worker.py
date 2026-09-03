import asyncio
import contextlib
import functools
import platform
import signal
import sys
from datetime import timedelta
from multiprocessing import Process

import sqlalchemy
from alembic import config, script
from alembic.runtime import migration
from dishka import AsyncContainer
from dishka.integrations.taskiq import setup_dishka
from taskiq import TaskiqEvents, TaskiqState
from taskiq.api import run_receiver_task, run_scheduler_task

from api import constants
from api.db import create_async_engine
from api.ioc import build_container
from api.ioc.worker import WorkerProvider
from api.logging import configure as configure_logging
from api.logging import get_logger
from api.sentry import configure_sentry
from api.services.coins import CoinService
from api.services.notification_manager import NotificationManager
from api.services.plugin_registry import PluginRegistry
from api.settings import Settings
from api.tasks import broker, scheduler
from api.types import TasksBroker
from api.utils.common import excepthook_handler, handle_event_loop_exception

logger = get_logger("worker")


def check_revision(conn: sqlalchemy.engine.Connection, script_dir: script.ScriptDirectory) -> bool:
    pass  # TODO: implement


async def check_db() -> bool:


async def lifespan_start(container: AsyncContainer, process: Process, state: TaskiqState) -> None:


async def lifespan_stop(container: AsyncContainer, state: TaskiqState) -> None:


def get_app(process: Process) -> TasksBroker:
    pass  # TODO: implement


async def _run_broker_core(broker: TasksBroker, stop_event: asyncio.Event | None) -> None:


async def start_broker_basic(broker: TasksBroker) -> None:


async def start_broker(broker: TasksBroker) -> None:


async def wait_loop() -> None:
