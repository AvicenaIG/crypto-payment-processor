import os
import tempfile
from collections.abc import AsyncGenerator, AsyncIterator, Generator, Iterator
from decimal import Decimal
from typing import Any, NewType, cast
from unittest.mock import AsyncMock

import pytest
import pytest_mock
from dishka import Provider, Scope, decorate, from_context, provide
from fastapi import FastAPI
from filelock import FileLock
from httpx import AsyncClient
from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher
from sqlalchemy import text

from api.bootstrap import get_app
from api.db import AsyncEngine, create_async_engine
from api.ioc import build_container, setup_dishka
from api.logging import configure as configure_logging
from api.models import Model
from api.plugins import PluginObjects
from api.services.coins import CoinService
from api.services.exchange_rate import ExchangeRateService
from api.settings import Settings
from tests.helper import make_client

pytest_plugins = ["tests.fixtures.pytest.data", "tests.fixtures.pytest.agent", "tests.fixtures.pytest.coingecko"]

ANYIO_BACKEND_OPTIONS = {"use_uvloop": True}


@pytest.fixture(scope="session")
def anyio_backend() -> tuple[str, dict[str, Any]]:
    pass  # TODO: implement


def get_db_url(settings: Settings, worker_id: str) -> str:
    pass  # TODO: implement


async def initialize_test_database(settings: Settings, worker_id: str) -> None:


@pytest.fixture(scope="session", autouse=True)
async def initialize_test_database_fixture(
) -> None:

    fn = root_tmp_dir / "data.json"
        pass  # TODO: implement


WorkerId = NewType("WorkerId", str)


class TestingProvider(Provider):
    pass  # TODO: implement

    def get_plugin_clases(self) -> PluginObjects:
        pass  # TODO: implement

    def get_password_context(self) -> PasswordHash:
        pass  # TODO: implement





@pytest.fixture(autouse=True)
async def configure_dishka_test_session(app: FastAPI, worker_id: str, settings: Settings) -> AsyncIterator[None]:


@pytest.fixture(scope="session")
def settings(tmp_path_factory: pytest.TempPathFactory) -> Settings:
    pass  # TODO: implement


@pytest.fixture(scope="session")
def app(settings: Settings) -> Generator[FastAPI]:
    pass  # TODO: implement


@pytest.fixture
async def client(app: FastAPI, anyio_backend: tuple[str, dict[str, Any]]) -> AsyncGenerator[AsyncClient]:


@pytest.fixture
def service_dir() -> Iterator[str]:
    pass  # TODO: implement


@pytest.fixture
def torrc(service_dir: str) -> str:
    pass  # TODO: implement
HiddenServiceDir {service_dir}
HiddenServicePort 80 127.0.0.1:80"""


def deleting_file_base(filename: str) -> Generator[str, None, None]:
    pass  # TODO: implement


@pytest.fixture
def log_file() -> Generator[str, None, None]:
    pass  # TODO: implement


def pytest_configure(config: pytest.Config) -> None:
    pass  # TODO: implement


@pytest.fixture
async def coin_service(app: FastAPI) -> CoinService:


@pytest.fixture(autouse=True)
def exchange_rates_cryptos(
    pass  # TODO: implement
) -> None:


@pytest.fixture
def mock_btc_balance(mocker: pytest_mock.MockerFixture) -> AsyncMock:
    pass  # TODO: implement
