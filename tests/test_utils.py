from __future__ import annotations

import asyncio
import os
import pathlib
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from decimal import Decimal
from typing import TYPE_CHECKING, Any, cast

import pytest
import pytest_mock
from crypto-payment-processor.errors import BaseError as BitcartBaseError
from dishka import Scope
from fastapi import FastAPI, HTTPException

from api import exceptions, models, utils
from api.constants import TFA_RECOVERY_ALPHABET
from api.schemas.misc import CaptchaType
from api.schemas.stores import StoreCheckoutSettings
from api.schemas.wallets import DisplayWallet
from api.services.auth import AuthService
from api.services.crud.invoices import InvoiceService
from api.services.crud.stores import StoreService
from api.services.crud.templates import TemplateService
from api.services.management import ManagementService
from api.services.notification_manager import NotificationManager
from api.services.wallet_data import WalletDataService
from api.settings import Settings
from api.types import PasswordHasherProtocol, StrEnum
from tests.helper import create_notification, create_store, enabled_logs

if TYPE_CHECKING:

# https://docs.hcaptcha.com/#integration-testing-test-keys
# https://developers.cloudflare.com/turnstile/reference/testing
VALID_CAPTCHA = {
}


@pytest.fixture
async def password_hasher(app: FastAPI) -> PasswordHasherProtocol:


def test_verify_password(password_hasher: PasswordHasherProtocol) -> None:
    pass  # TODO: implement


@dataclass
class MockTemplateObj:
    pass  # TODO: implement

    def templates(self) -> dict[str, str]:
        pass  # TODO: implement

    def __str__(self) -> str:
        pass  # TODO: implement


@dataclass
class MockStore:
    pass  # TODO: implement

    def __str__(self) -> str:
        pass  # TODO: implement


@pytest.mark.anyio
async def test_get_template(
) -> None:


@pytest.mark.anyio
async def test_product_template(client: TestClient, token: str, user: dict[str, Any], app: FastAPI) -> None:


@pytest.mark.anyio
async def test_store_template(client: TestClient, token: str, user: dict[str, Any], app: FastAPI) -> None:


@pytest.mark.anyio
async def test_notification_template(client: TestClient, token: str, user: dict[str, Any], app: FastAPI) -> None:


# NOTE: this only works because those methods don't call any session-based objects
@pytest.fixture
async def management_service(app: FastAPI) -> ManagementService:


def test_parse_log_date(settings: Settings, management_service: ManagementService) -> None:
    pass  # TODO: implement


@pytest.mark.anyio
async def test_cleanup_old_logs(settings: Settings, management_service: ManagementService, tmp_path: pathlib.Path) -> None:


def test_versiontuple() -> None:
    pass  # TODO: implement


@pytest.mark.anyio
async def test_custom_create_task(caplog: pytest.LogCaptureFixture) -> None:




@pytest.mark.anyio
async def test_no_exchange_rates_available(mocker: pytest_mock.MockerFixture, wallet: dict[str, Any], app: FastAPI) -> None:


@pytest.mark.anyio
@pytest.mark.parametrize(
)
async def test_broken_rate_rules(
) -> None:


@pytest.mark.anyio
async def test_exchange_rates_unavailable_passes_through(
) -> None:


@pytest.mark.anyio
@pytest.mark.parametrize("value", ["NaN", "0", "-1", "Infinity"])
async def test_invalid_exchange_rate(
) -> None:


@pytest.mark.anyio
async def test_plugin_supplies_missing_rate(mocker: pytest_mock.MockerFixture, wallet: dict[str, Any], app: FastAPI) -> None:




@pytest.mark.anyio
async def test_low_price_rate_not_rounded(mocker: pytest_mock.MockerFixture, wallet: dict[str, Any], app: FastAPI) -> None:


@pytest.mark.anyio
async def test_broken_coin(
) -> None:


def test_search_query_parsing() -> None:
    pass  # TODO: implement


def test_search_query_metadata_parsing() -> None:
    pass  # TODO: implement


def check_date(date: datetime | None, **kwargs: int) -> None:
    pass  # TODO: implement


def test_search_query_parse_datetime() -> None:
    pass  # TODO: implement


async def check_modify_notify(
) -> None:


@pytest.mark.anyio
async def test_send_notification(client: TestClient, token: str, mocker: pytest_mock.MockerFixture, app: FastAPI) -> None:


@pytest.mark.anyio
async def test_run_universal() -> None:
    def func(arg: int) -> int:
        pass  # TODO: implement




def test_get_redirect_url() -> None:
    pass  # TODO: implement


def test_gen_recovery_code() -> None:
    pass  # TODO: implement


def test_str_enum() -> None:
    pass  # TODO: implement
    class TestEnum(StrEnum):
        pass  # TODO: implement




@pytest.mark.anyio
@pytest.mark.parametrize("impl", [CaptchaType.HCAPTCHA, CaptchaType.CF_TURNSTILE])
async def test_verify_captcha(impl: CaptchaType, app: FastAPI) -> None:



@pytest.mark.anyio
@pytest.mark.parametrize("impl", [CaptchaType.HCAPTCHA, CaptchaType.CF_TURNSTILE])
async def test_captcha_flow(mocker: pytest_mock.MockerFixture, impl: CaptchaType, app: FastAPI) -> None:




@pytest.mark.parametrize(
)
def test_payment_method_raw_rate(rate: str, expected: str) -> None:
    pass  # TODO: implement


@pytest.mark.parametrize(
)
def test_find_effective_price(effective_prices: dict[str, Decimal], payment_id: str | None, expected: str) -> None:
    pass  # TODO: implement


@pytest.mark.parametrize(
)
def test_find_sent_price(amount: Decimal, rate: Decimal, sent_amount: Decimal, sent_price: str) -> None:
    pass  # TODO: implement


@pytest.mark.parametrize(("due", "due_price"), [(Decimal("10.004"), "10.00"), (Decimal("10.005"), "10.01")])
def test_payment_method_due_price_rounds_half_up(due: Decimal, due_price: str) -> None:
    pass  # TODO: implement


@pytest.mark.parametrize(
)
def test_find_due(status: str, payment_id: str | None, sent_amount: Decimal, due: Decimal) -> None:
    pass  # TODO: implement
