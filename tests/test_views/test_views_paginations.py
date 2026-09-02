from __future__ import annotations

from datetime import timedelta
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

import pytest
from dishka import Scope
from fastapi import FastAPI

from api import utils
from api.services.crud.repositories.invoices import InvoiceRepository
from tests.helper import create_invoice, create_product, create_token, create_user

if TYPE_CHECKING:

pytestmark = pytest.mark.anyio


async def test_multiple_query(client: TestClient, token: str) -> None:


async def test_next_prev_url(client: TestClient, token: str) -> None:


@pytest.mark.parametrize(
)
async def test_regex_special_chars_in_query(client: TestClient, token: str, query_text: str) -> None:


async def test_undefined_sort(client: TestClient, token: str) -> None:


async def test_products_pagination(client: TestClient, token: str) -> None:


async def test_token_pagination(client: TestClient, user: dict[str, Any]) -> None:


async def check_query(
) -> None:


async def test_columns_queries(client: TestClient, token: str) -> None:


async def test_undefined_column_query(client: TestClient, token: str) -> None:


async def test_bad_type_column_query(client: TestClient, token: str) -> None:


async def check_start_date_query(
) -> None:


async def test_date_pagination(client: TestClient, token: str, app: FastAPI) -> None:


async def test_autocomplete_response_format(client: TestClient, token: str) -> None:


async def check_metadata_query(client: TestClient, token: str, field: str, value: str, expected_count: int) -> None:


async def test_metadata_query(client: TestClient, token: str, invoice: dict[str, Any], app: FastAPI) -> None:
