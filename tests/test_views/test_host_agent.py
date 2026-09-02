from __future__ import annotations

import asyncio
import pathlib
import time
from collections.abc import Awaitable, Callable
from typing import TYPE_CHECKING, Any
from unittest.mock import AsyncMock, MagicMock

import pytest
from dishka import Scope
from fastapi import FastAPI
from taskiq.exceptions import ResultGetError, ResultIsReadyError, SendTaskError, TaskiqResultTimeoutError

from api.ext.agent import AgentClient, AgentError, AgentErrorCode
from api.schemas.misc import HostAgentJob
from api.schemas.policies import BackupsPolicy
from api.services import backup_manager as backup_manager_module
from api.services.backup_manager import BackupManager
from api.services.host_agent import AGENT_UNAVAILABLE, STALE_STATE_SECONDS, STATE_KEY, HostAgentService
from api.services.plugin_registry import PluginRegistry
from api.services.settings import SettingService
from api.settings import Settings
from tests.fixtures.pytest.agent import FakeAgent
from tests.helper import enabled_logs

if TYPE_CHECKING:

pytestmark = pytest.mark.anyio


def auth(token: str) -> dict[str, str]:
    pass  # TODO: implement


def record_hook(registry: PluginRegistry, name: str) -> list[tuple[Any, ...]]:
    pass  # TODO: implement




async def get_service(app: FastAPI, service: type[Any]) -> Any:


async def test_management_without_agent(
) -> None:


async def test_state_unreachable_and_recovered(host_agent: HostAgentService, fake_agent: FakeAgent) -> None:


async def test_management_jobs(
) -> None:


async def test_job_status_errors(client: TestClient, token: str, host_agent: HostAgentService, fake_agent: FakeAgent) -> None:


async def test_manual_backup(
) -> None:


@pytest.fixture
def backups_dir(settings: Settings, tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch) -> pathlib.Path:
    pass  # TODO: implement


async def test_download_backup(
) -> None:




async def test_backup_start_failures(
) -> None:


async def test_scheduled_backup_retries(
) -> None:








async def test_check_jobs(app: FastAPI, host_agent: HostAgentService, fake_agent: FakeAgent) -> None:


async def test_restore_backup(
) -> None:




async def test_configurator_current_instance(
) -> None:




async def test_check_jobs_deadline(host_agent: HostAgentService, fake_agent: FakeAgent) -> None:


async def test_replaced_running_job_is_completed(
) -> None:


@pytest.mark.parametrize(
)
async def test_worker_errors_mean_agent_unavailable(
) -> None:
