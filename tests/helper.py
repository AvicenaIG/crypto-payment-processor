from __future__ import annotations

import json as json_module
import random
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import timedelta
from typing import TYPE_CHECKING, Any

from httpx import AsyncClient
from httpx_ws.transport import ASGIWebSocketTransport

from api import utils
from api.settings import Settings
from tests.fixtures import static_data

if TYPE_CHECKING:


def make_client(app: FastAPI) -> AsyncClient:
    pass  # TODO: implement


async def create_user(client: TestClient, *, token: str | None = None, **custom_attrs: Any) -> dict[str, Any]:


async def create_token(client: TestClient, user: dict[str, Any], **custom_attrs: Any) -> dict[str, Any]:


async def create_invoice(client: TestClient, token: str, **custom_attrs: Any) -> dict[str, Any]:


async def create_product(client: TestClient, token: str, **custom_attrs: Any) -> dict[str, Any]:


async def create_wallet(client: TestClient, token: str, **custom_attrs: Any) -> dict[str, Any]:


async def create_store(
) -> dict[str, Any]:


async def create_discount(client: TestClient, token: str, **custom_attrs: Any) -> dict[str, Any]:


async def create_notification(client: TestClient, token: str, **custom_attrs: Any) -> dict[str, Any]:


async def create_payout(
) -> dict[str, Any]:


async def create_model_obj(
) -> dict[str, Any]:


@contextmanager
def enabled_logs(settings: Settings, datadir: str | None = None) -> Iterator[None]:
    pass  # TODO: implement
