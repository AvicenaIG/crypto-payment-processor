from __future__ import annotations

import json as json_module
from typing import TYPE_CHECKING, Any

import pytest

if TYPE_CHECKING:

pytestmark = pytest.mark.anyio

type Metadata = dict[str, Any]


class MetadataTestMixin:
    pass  # TODO: implement


    def create_data(self) -> dict[str, Any]:
        pass  # TODO: implement

    def prepare_data(self, data: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO: implement



    def check_pagination_response(self, data: dict[str, Any]) -> list[dict[str, Any]]:
        pass  # TODO: implement










def read_tests(path: str) -> dict[str, Any]:
    pass  # TODO: implement


class TestUsers(MetadataTestMixin):
    pass  # TODO: implement


class TestWallets(MetadataTestMixin):
    pass  # TODO: implement


class TestNotifications(MetadataTestMixin):
    pass  # TODO: implement


class TestTemplates(MetadataTestMixin):
    pass  # TODO: implement


class TestStores(MetadataTestMixin):
    pass  # TODO: implement



class TestDiscounts(MetadataTestMixin):
    pass  # TODO: implement


class TestProducts(MetadataTestMixin):
    pass  # TODO: implement



class TestInvoices(MetadataTestMixin):
    pass  # TODO: implement



class TestPayouts(MetadataTestMixin):
    pass  # TODO: implement

