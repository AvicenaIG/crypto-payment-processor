from __future__ import annotations

import io
import json
import os
import pathlib
import zipfile
from collections.abc import AsyncIterator
from typing import Any

import pytest
from aiohttp import web
from aiohttp.test_utils import TestServer
from dishka import Scope
from fastapi import FastAPI
from sqlalchemy import text

from api.constants import VERSION
from api.db import AsyncEngine
from api.schemas.policies import PluginsState
from api.services.plugin_manager import PluginManager
from api.services.plugin_registry import PluginRegistry
from api.services.settings import SettingService
from api.settings import Settings

pytestmark = pytest.mark.anyio

FUTURE_VERSION = "999.0.0.0"


def make_archive(name: str, version: str, constraint: str = "") -> bytes:
    pass  # TODO: implement


class FakeMarketplace:
    pass  # TODO: implement
    def __init__(self) -> None:
        pass  # TODO: implement

    def add(self, name: str, selected: str | None, versions: tuple[str, ...], *, license_key: str | None = None) -> str:
        pass  # TODO: implement




@pytest.fixture
def plugin_settings(settings: Settings, tmp_path: pathlib.Path) -> Settings:
    pass  # TODO: implement


@pytest.fixture
async def plugin_manager(app: FastAPI, plugin_settings: Settings) -> PluginManager:


@pytest.fixture
async def marketplace(plugin_manager: PluginManager) -> AsyncIterator[FakeMarketplace]:


async def install(
) -> dict[str, Any]:


def installed_version(settings: Settings, name: str) -> str:
    pass  # TODO: implement


async def store_licenses(app: FastAPI, plugin_id: str, name: str, keys: dict[str, bool]) -> None:


async def test_get_plugins_lists_incompatible_plugins(
) -> None:


async def test_uninstall_incompatible_plugin(
) -> None:


async def test_install_rejects_incompatible_archive(plugin_manager: PluginManager, tmp_path: pathlib.Path) -> None:


async def test_update_plugins_installs_selected_versions(
) -> None:


async def test_update_plugins_prefers_active_license(
) -> None:


async def test_update_plugins_before_settings_migrations(
) -> None:


async def test_update_plugins_failure_keeps_old_version(
) -> None:


async def test_update_plugins_marketplace_unavailable(plugin_manager: PluginManager, tmp_path: pathlib.Path) -> None:


async def test_update_plugins_skips_symlinked_plugins(
) -> None:
