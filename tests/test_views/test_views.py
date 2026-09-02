from __future__ import annotations

import asyncio
import json as json_module
import os
import socket
from collections import defaultdict
from datetime import datetime, timedelta
from decimal import Decimal
from typing import TYPE_CHECKING, Any, cast

import paramiko
import pyotp
import pytest
import pytest_mock
from crypto-payment-processor import BTC, LTC  # type: ignore
from crypto-payment-processor.errors import BaseError as BitcartBaseError
from dishka import Scope
from fastapi import FastAPI
from httpx import Request as HttpRequest
from httpx_ws import AsyncWebSocketSession, WebSocketDisconnect, aconnect_ws
from redis.observability.attributes import DB_CLIENT_CONNECTION_STATE, ConnectionState
from sqlalchemy import select
from starlette.status import WS_1008_POLICY_VIOLATION
from taskiq.exceptions import TaskiqResultTimeoutError

from api import models, utils
from api.constants import (
)
from api.exceptions import ExchangeRatesUnavailableError, RateUnavailableError
from api.invoices import InvoiceStatus
from api.redis import Redis
from api.schemas.misc import CaptchaType, EmailSettings
from api.schemas.stores import StoreCheckoutSettings, StoreThemeSettings
from api.schemas.users import UserPreferences
from api.services.coins import CoinService
from api.services.crud.invoices import InvoiceService
from api.services.crud.payouts import PayoutService
from api.services.crud.refunds import RefundService
from api.services.crud.repositories import PaymentMethodRepository
from api.services.ext.configurator import SSH_RATE_KEY
from api.services.ext.tor import TorService
from api.services.notification_manager import NotificationManager
from api.services.payment_processor import PaymentProcessor
from api.services.payout_manager import PayoutManager
from api.settings import Settings
from api.templates import TemplateManager
from api.types import Quotes, TasksBroker
from tests.fixtures import static_data
from tests.helper import (
)

if TYPE_CHECKING:

pytestmark = pytest.mark.anyio

settings = Settings()
MAIN_PORT = settings.config("BTC_PORT", cast=int, default=5000)
MAIN_URL = f"http://localhost:{MAIN_PORT}"
del settings


class DummyInstance:
    pass  # TODO: implement


async def test_docs_root(client: TestClient) -> None:


async def test_rate(client: TestClient) -> None:


@pytest.mark.parametrize("value", ["0", "-1", "Infinity"])
async def test_rate_invalid(client: TestClient, mocker: pytest_mock.MockerFixture, value: str) -> None:


async def test_wallet_rate(client: TestClient, token: str, wallet: dict[str, Any]) -> None:


@pytest.mark.parametrize(
)
async def test_create_token(client: TestClient, user: dict[str, Any], user_exists: bool, correct_pwd: bool) -> None:


async def test_noauth(client: TestClient) -> None:


async def test_superuseronly(client: TestClient, token: str, limited_token: str) -> None:


async def test_users_me(client: TestClient, user: dict[str, Any], token: str) -> None:


def mock_missing_rate(exchange: str, pair: str | None = None) -> Decimal | Quotes:
    pass  # TODO: implement


async def test_wallets_balance(client: TestClient, token: str, wallet: dict[str, Any], mock_btc_balance: Any) -> None:


async def test_wallets_balance_missing_rates(
) -> None:


async def test_wallets_balance_skips_empty_wallets(
) -> None:


async def test_ratesinfo(client: TestClient, token: str, limited_token: str) -> None:


async def test_rates_worker_unavailable(
) -> None:


async def test_invoice_logs_rates_unavailable_cause(
) -> None:
    def unavailable(*args: Any, **kwargs: Any) -> None:
        pass  # TODO: implement



async def test_failed_rate_rules_not_saved(
) -> None:


async def test_store_rates(client: TestClient, token: str, store: dict[str, Any]) -> None:


async def test_fiatlist(client: TestClient) -> None:


@pytest.mark.exchange_rates(cryptos={"btc": BTC(), "ltc": LTC()})
async def test_fiatlist_multi_coins(client: TestClient) -> None:


async def check_ws_response(ws: AsyncWebSocketSession, sent_amount: Decimal | int) -> None:


async def check_ws_response_complete(ws: AsyncWebSocketSession, sent_amount: Decimal | int) -> None:


async def check_ws_response2(ws: AsyncWebSocketSession) -> None:


@pytest.mark.parametrize(
)
async def test_ping_email(client: TestClient, token: str, store: dict[str, Any], store_exists: bool, authorized: bool) -> None:


async def test_user_stats(client: TestClient, token: str, store: dict[str, Any]) -> None:


@pytest.mark.parametrize(
)
async def test_categories(client: TestClient, token: str, categories: list[str], store: dict[str, Any]) -> None:


async def test_token(client: TestClient, token_data: dict[str, Any]) -> None:


async def test_token_current(client: TestClient, token: str, user: dict[str, Any]) -> None:


async def test_token_count(client: TestClient, token: str) -> None:


async def test_patch_token(client: TestClient, token: str) -> None:


@pytest.mark.parametrize(
)
async def test_create_tokens(
) -> None:


async def test_token_permissions_control(
) -> None:


@pytest.mark.parametrize(
)
async def test_delete_token(client: TestClient, token: str, token_exists: bool, authorized: bool) -> None:


async def test_management_commands(
) -> None:


async def test_first_user_registration_bypasses_disable_registration(client: TestClient) -> None:


async def test_policies(client: TestClient, token: str) -> None:


async def test_policies_store_created(client: TestClient, store: dict[str, Any]) -> None:


async def test_no_token_management(client: TestClient, limited_token: str) -> None:


async def test_non_superuser_permissions(client: TestClient, user: dict[str, Any], limited_user: dict[str, Any]) -> None:


async def test_notification_list(client: TestClient, app: FastAPI) -> None:


async def test_notification_schema(client: TestClient, app: FastAPI) -> None:


async def test_template_list(client: TestClient, app: FastAPI) -> None:


async def test_services(client: TestClient, token: str, app: FastAPI) -> None:


async def test_export_invoices(client: TestClient, token: str, limited_user: dict[str, Any]) -> None:


async def test_batch_commands(client: TestClient, token: str, store: dict[str, Any]) -> None:


async def test_wallet_ws(client: TestClient, token: str, app: FastAPI, mock_btc_balance: Any) -> None:


async def test_invoice_ws(client: TestClient, token: str, store: dict[str, Any], app: FastAPI) -> None:


def get_in_use_connections(redis_pool: Redis) -> int:
    pass  # TODO: implement


async def test_ws_releases_redis_connections(client: TestClient, token: str, store: dict[str, Any], app: FastAPI) -> None:


@pytest.mark.parametrize("currencies", ["", "DUMMY", "btc"])
async def test_create_invoice_discount(client: TestClient, token: str, store: dict[str, Any], currencies: str) -> None:


async def test_get_or_create_invoice_by_order_id(client: TestClient, token: str, store: dict[str, Any], app: FastAPI) -> None:


async def test_get_max_product_price(client: TestClient, token: str, store: dict[str, Any]) -> None:


async def test_create_product_with_image(
) -> None:


async def test_create_invoice_without_coin_rate(
) -> None:


@pytest.mark.parametrize(
)
async def test_create_invoice_rate(
) -> None:


@pytest.mark.parametrize(
)
async def test_create_invoice_underpaid_amount(
) -> None:


async def enable_network_fee(client: TestClient, token: str, store: dict[str, Any]) -> None:


async def create_discounted_invoice(
) -> dict[str, Any]:


async def test_create_invoice_network_fee(
) -> None:


async def test_payment_discount_snapshot(client: TestClient, token: str, store: dict[str, Any]) -> None:


@pytest.mark.parametrize(("percent", "effective_price"), [(None, "5000.00"), (10, "4500.00")])
async def test_invoice_effective_price(
) -> None:


@pytest.mark.parametrize(
)
async def test_invoice_transactions(
) -> None:


async def test_new_block_keeps_transactions(
) -> None:


@pytest.mark.parametrize(("sent_amount", "exception_status"), [(0.09, "none"), (0.1, "none"), (0.11, "paid_over")])
async def test_mark_complete_exception_status(
) -> None:


@pytest.mark.parametrize(("options", "sent_price"), [({}, "5000.00"), ({"sent_amount": 0.05}, "2500.00")])
async def test_invoice_sent_price(
) -> None:


async def test_invoice_payment_due(client: TestClient, token: str, store: dict[str, Any], app: FastAPI) -> None:


async def test_lightning_payment_method_amount(
) -> None:


@pytest.mark.parametrize(
)
async def test_create_invoice_network_fee_failure(
) -> None:


async def send_payouts(client: TestClient, token: str, ids: list[str], options: dict[str, Any] | None = None) -> None:


async def create_store_payout(client: TestClient, token: str, store: dict[str, Any], **attrs: Any) -> str:


async def mark_payout_sent(app: FastAPI, payout_id: str, tx_hash: str) -> None:


async def get_payout_state(client: TestClient, token: str, payout_id: str) -> tuple[str, str | None]:


async def test_payout_used_fee_in_wallet_currency(client: TestClient, token: str, app: FastAPI) -> None:


async def test_payout_fails_without_rate(client: TestClient, token: str, mocker: pytest_mock.MockerFixture) -> None:


async def test_batch_payout_max_fee_per_payout_rate(
) -> None:


async def test_batch_payout_skips_sent_payouts(
) -> None:


async def test_failed_batch_payout_keeps_sent_payouts(
) -> None:


async def test_create_invoice_and_pay(client: TestClient, token: str, store: dict[str, Any], app: FastAPI) -> None:


async def test_get_public_store(client: TestClient, store: dict[str, Any], token: str) -> None:


async def test_public_store_support_contact(client: TestClient, store: dict[str, Any], token: str) -> None:


# TODO: why do we need ?store=X in this case?
async def test_get_product_params(client: TestClient, token: str, product: dict[str, Any]) -> None:


async def test_product_count_params(client: TestClient, token: str) -> None:


async def test_updatecheck(client: TestClient) -> None:


async def test_logs_list(client: TestClient, token: str, settings: Settings) -> None:


async def test_logs_get(client: TestClient, token: str, settings: Settings) -> None:


async def test_logs_delete(client: TestClient, log_file: str, token: str, settings: Settings) -> None:


async def test_cryptos(client: TestClient, app: FastAPI) -> None:


async def test_wallet_balance(client: TestClient, token: str, wallet: dict[str, Any], mock_btc_balance: Any) -> None:


async def test_lightning_endpoints(client: TestClient, token: str, wallet: dict[str, Any]) -> None:


async def test_multiple_wallets_same_currency(client: TestClient, token: str) -> None:


async def test_change_store_checkout_settings(client: TestClient, token: str, store: dict[str, Any]) -> None:


async def test_change_store_theme_settings(client: TestClient, token: str, store: dict[str, Any]) -> None:


async def test_products_list(client: TestClient) -> None:


PUBLIC_IP = "93.184.215.14"
PUBLIC_HOST = "shop.example.com"
INTERNAL_DNS = {
}
FAKE_DNS = {**INTERNAL_DNS, PUBLIC_HOST: ["172.18.0.7", PUBLIC_IP]}
SSH_SETTINGS = {"host": PUBLIC_HOST, "username": "root", "password": "password"}
INTERNAL_HOSTS = ("", "localhost", "127.0.0.1", "0x7f000001", "::1", "10.0.0.1", "nonexistent.invalid", *INTERNAL_DNS)


def make_addrinfo(*addresses: str) -> list[Any]:
    pass  # TODO: implement


@pytest.fixture
def fake_dns(mocker: pytest_mock.MockerFixture) -> None:
    pass  # TODO: implement

    def getaddrinfo(host: str, *args: Any, **kwargs: Any) -> list[Any]:
        pass  # TODO: implement



@pytest.mark.usefixtures("fake_dns")
async def test_configurator(app: FastAPI, client: TestClient, token: str, mocker: pytest_mock.MockerFixture) -> None:


async def test_supported_cryptos(client: TestClient) -> None:


@pytest.mark.usefixtures("fake_dns")
async def test_get_server_settings(client: TestClient, token: str, mocker: pytest_mock.MockerFixture) -> None:


async def test_get_server_settings_dns_rebinding(client: TestClient, mocker: pytest_mock.MockerFixture) -> None:

    def getaddrinfo(host: str, *args: Any, **kwargs: Any) -> list[Any]:
        pass  # TODO: implement



async def test_configurator_ssh_rate_limit(app: FastAPI, client: TestClient, mocker: pytest_mock.MockerFixture) -> None:




async def test_unauthorized_m2m_access(
) -> None:


async def get_wallet_balances(client: TestClient, token: str) -> str:


async def test_users_display_balance(client: TestClient, token: str, wallet: dict[str, Any], mock_btc_balance: Any) -> None:


async def test_invoice_products_access_control(client: TestClient) -> None:


async def test_wallets_labels(client: TestClient, token: str) -> None:


async def test_backup_providers(client: TestClient) -> None:


async def test_backup_frequencies(client: TestClient) -> None:


async def test_backup_policies(client: TestClient, token: str) -> None:


async def test_products_pagination_deleted_store(client: TestClient, token: str, store: dict[str, Any]) -> None:


@pytest.mark.parametrize(
)
async def test_invoice_update_customer(client: TestClient, token: str, name: str, expected: str, updated: str) -> None:


async def test_get_tokens_btc(client: TestClient) -> None:


class NotRunningBTC:
    pass  # TODO: implement

    class server:
        pass  # TODO: implement
        def getinfo() -> None:
            pass  # TODO: implement


async def test_syncinfo(client: TestClient, token: str, mocker: pytest_mock.MockerFixture) -> None:
    def find_element(elements: list[dict[str, Any]], name: str) -> dict[str, Any]:
        pass  # TODO: implement



async def test_create_invoice_randomize_wallets(client: TestClient, token: str) -> None:


async def test_get_default_explorer(client: TestClient) -> None:


async def test_get_default_rpc(client: TestClient) -> None:


async def test_invoices_authorized_access(client: TestClient, store: dict[str, Any], token: str) -> None:


async def test_wallet_schema(client: TestClient) -> None:


async def test_invoices_payment_details(client: TestClient, token: str) -> None:


async def test_ping_server_mail(client: TestClient, token: str) -> None:


async def test_password_reset(client: TestClient, user: dict[str, Any], token: str, mocker: pytest_mock.MockerFixture) -> None:

    def func(url: str, code: str) -> None:
        pass  # TODO: implement



async def test_products_quantity_management(client: TestClient, token: str, store: dict[str, Any]) -> None:


async def test_configurator_dns_resolve(client: TestClient, token: str) -> None:


@pytest.mark.usefixtures("fake_dns")
async def test_configurator_dns_resolve_hides_internal_names(client: TestClient) -> None:


async def test_tfa_flow(client: TestClient, user: dict[str, Any], token: str) -> None:


async def test_verify_email(client: TestClient, user: dict[str, Any], token: str, mocker: pytest_mock.MockerFixture) -> None:

    def func(url: str, code: str) -> None:
        pass  # TODO: implement



async def test_token_verification(client: TestClient, user: dict[str, Any], token: str) -> None:


async def test_reset_password(client: TestClient, token: str) -> None:


async def test_files_functionality(client: TestClient, token: str, limited_user: dict[str, Any], settings: Settings) -> None:


async def test_generate_wallet(client: TestClient, token: str) -> None:


async def test_refund_functionality(client: TestClient, token: str, mocker: pytest_mock.MockerFixture, app: FastAPI) -> None:




async def test_refund_amount_rounded_down(client: TestClient, token: str, app: FastAPI) -> None:


async def test_refund_with_deleted_invoice(client: TestClient, token: str, app: FastAPI) -> None:


async def test_wallet_symbol(client: TestClient, token: str, wallet: dict[str, Any]) -> None:


async def test_invoice_custom_payment_methods(client: TestClient, token: str) -> None:


@pytest.mark.parametrize(
)
async def test_mark_complete_cases(
) -> None:


@pytest.mark.parametrize(
)
async def test_mark_complete_transactions(
) -> None:


async def test_mark_complete_validation(client: TestClient, token: str, store: dict[str, Any]) -> None:
