from __future__ import annotations

import json as json_module
from datetime import datetime
from typing import TYPE_CHECKING, Any

import pytest

from api.constants import ID_LENGTH

if TYPE_CHECKING:


pytestmark = pytest.mark.anyio


def assert_contains(expected: dict[str, Any], actual: dict[str, Any]) -> None:
    pass  # TODO: implement


class ViewTestMixin:
    pass  # TODO: implement





    def state(self) -> dict[str, Any]:
        pass  # TODO: implement


    def object_id(self, state: dict[str, Any]) -> str:
        pass  # TODO: implement

    def create_data(self, state: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO: implement

    def patch_data(self) -> dict[str, Any]:
        pass  # TODO: implement

    def expected_resp(self, state: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO: implement

    def expected_count(self) -> int:
        pass  # TODO: implement


    def check_pagination_response(self, data: dict[str, Any]) -> list[dict[str, Any]]:
        pass  # TODO: implement

    def _check_key(self, data: dict[str, Any], key: str, key_type: type) -> None:
        pass  # TODO: implement

    def check_id(self, data: dict[str, Any], id_length: int) -> None:
        pass  # TODO: implement

    def check_created(self, data: dict[str, Any]) -> None:
        pass  # TODO: implement

    def check_data(self, data: dict[str, Any]) -> None:
        pass  # TODO: implement


    def prepare_data(self, data: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO: implement




    def get_computed_fields(self) -> set[str]:
        pass  # TODO: implement






def read_tests(path: str) -> dict[str, Any]:
    pass  # TODO: implement


class TestUsers(ViewTestMixin):
    pass  # TODO: implement


class TestWallets(ViewTestMixin):
    pass  # TODO: implement


class TestNotifications(ViewTestMixin):
    pass  # TODO: implement



class TestTemplates(ViewTestMixin):
    pass  # TODO: implement



class TestStores(ViewTestMixin):
    pass  # TODO: implement


    def _add_related(self, data: dict[str, Any], state: dict[str, Any]) -> None:
        pass  # TODO: implement

    def create_data(self, state: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO: implement

    def expected_resp(self, state: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO: implement


class TestDiscounts(ViewTestMixin):
    pass  # TODO: implement



class TestProducts(ViewTestMixin):
    pass  # TODO: implement


    def _add_related(self, data: dict[str, Any], state: dict[str, Any]) -> None:
        pass  # TODO: implement

    def create_data(self, state: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO: implement

    def expected_resp(self, state: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO: implement


class TestInvoices(ViewTestMixin):
    pass  # TODO: implement


    def _add_related(self, data: dict[str, Any], state: dict[str, Any]) -> None:
        pass  # TODO: implement

    def create_data(self, state: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO: implement

    def expected_resp(self, state: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO: implement

    def check_data(self, data: dict[str, Any]) -> None:
        pass  # TODO: implement

    def check_payments(self, data: dict[str, Any]) -> None:
        pass  # TODO: implement


class TestPayouts(ViewTestMixin):
    pass  # TODO: implement


    def _add_related(self, data: dict[str, Any], state: dict[str, Any]) -> None:
        pass  # TODO: implement

    def create_data(self, state: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO: implement

    def expected_resp(self, state: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO: implement
