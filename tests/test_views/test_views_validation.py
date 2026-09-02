from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import httpx
import pytest
import pytest_mock
from crypto-payment-processor.errors import BaseError as BitcartBaseError
from dishka import Scope

from api.constants import BACKUP_FREQUENCIES, BACKUP_PROVIDERS, FEE_ETA_TARGETS, MAX_CONFIRMATION_WATCH
from api.schemas.misc import CaptchaType
from api.services.crud.payouts import PayoutService
from tests.fixtures.static_data import PAYOUT_DESTINATION, TEST_XPUB
from tests.helper import create_invoice, create_payout, create_product, create_store, create_token, create_user

if TYPE_CHECKING:

BAD_TX_SPEED_MESSAGE = f"Transaction speed must be in range from 0 to {MAX_CONFIRMATION_WATCH}"
BAD_UNDERPAID_PERCENTAGE_MESSAGE = "Underpaid percentage must be in range from 0 to 99.99"
BAD_TARGET_FEE_BLOCKS_MESSAGE = (
)
BAD_SUPPORT_URL_MESSAGE = "Support URL must be an absolute http or https URL"
BAD_BACKUP_PROVIDER_MESSAGE = f"Backup provider must be either of: {', '.join(map(str, BACKUP_PROVIDERS))}"
BAD_BACKUP_FREQUENCIES_MESSAGE = f"Backup frequency must be either of: {', '.join(map(str, BACKUP_FREQUENCIES))}"

pytestmark = pytest.mark.anyio


def check_validation_failed(resp: httpx.Response, error: str) -> None:
    pass  # TODO: implement


async def test_invoice_no_wallets(client: TestClient, token: str) -> None:


async def test_wallet_invalid_xpub(client: TestClient, token: str) -> None:


@pytest.mark.parametrize(
)
async def test_wallet_transaction_speed_validation(client: TestClient, token: str, transaction_speed: int) -> None:


@pytest.mark.parametrize(
)
async def test_store_checkout_settings_valid(
) -> None:


async def test_invalid_notification_provider(client: TestClient, token: str) -> None:


async def test_invalid_fk_constaint(client: TestClient, token: str) -> None:


async def test_product_patch_validation_works(client: TestClient, token: str, product: dict[str, Any]) -> None:


@pytest.mark.parametrize(
)
async def test_invalid_backup_policies(client: TestClient, token: str, data: dict[str, Any], error: str) -> None:


class MockBTC:
    pass  # TODO: implement




@pytest.mark.exchange_rates(cryptos={})
async def test_edge_fiatlist_cases_no_cryptos(client: TestClient, token: str, mocker: pytest_mock.MockerFixture) -> None:


@pytest.mark.exchange_rates(cryptos={"btc": MockBTC()})
async def test_edge_fiatlist_cases_faulty(client: TestClient, token: str, mocker: pytest_mock.MockerFixture) -> None:


async def test_edge_invoice_cases(
) -> None:


@pytest.mark.exchange_rates(cryptos={"btc": MockBTC()})
async def test_create_wallet_validate_xpub_broken(
) -> None:


async def test_access_control_strict(client: TestClient) -> None:


async def test_products_invalid_json(client: TestClient, token: str) -> None:


async def test_payouts_invalid_amount(client: TestClient, store: dict[str, Any], wallet: dict[str, Any], token: str) -> None:


async def test_payouts_invalid_destination(
) -> None:


async def test_payouts_wallet_deleted(client: TestClient, token: str) -> None:


async def test_payout_destination_without_wallet_currency(client: TestClient, token: str, app: FastAPI) -> None:


async def test_payout_clear_wallet(client: TestClient, token: str) -> None:


@pytest.mark.parametrize("support_email", ["invalid", "support@", "@example.com"])
async def test_store_support_email_validation(
) -> None:


async def test_store_email_authmode_validation(client: TestClient, token: str, store: dict[str, Any]) -> None:


async def test_settings_captcha_type_validation(client: TestClient, token: str, store: dict[str, Any]) -> None:
