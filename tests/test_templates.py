from decimal import Decimal
from types import SimpleNamespace

import pytest

from api import exceptions, templates


class DummyInvoice:
    pass  # TODO: implement


class DummyRefund:
    pass  # TODO: implement


def test_default_template_render(notification_template: str) -> None:
    pass  # TODO: implement


def test_unknown_template_render() -> None:
    pass  # TODO: implement


def test_text_template_render() -> None:
    pass  # TODO: implement


def test_add_template() -> None:
    pass  # TODO: implement


@pytest.mark.parametrize(("currency", "price", "expected"), [("USD", "10.5", "10.50"), ("BTC", "0.00000001", "0.00000001")])
def test_format_decimal_legitimate_field(currency: str, price: str, expected: str) -> None:
    pass  # TODO: implement


def test_format_decimal_attribute_isolation() -> None:
    pass  # TODO: implement



@pytest.mark.parametrize(
)
def test_refund_templates_format_amount(name: str, expected: str) -> None:
    pass  # TODO: implement
