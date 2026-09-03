import glob
import importlib
import os
from abc import ABCMeta, abstractmethod
from collections.abc import Callable
from decimal import Decimal
from typing import TYPE_CHECKING, Any, NewType, cast

from dishka import AsyncContainer as DIContainer
from dishka import FromDishka as FromDI
from dishka import Provider
from dishka import Scope as DIScope
from dishka.integrations.fastapi import DishkaRoute as DIRoute
from fastapi import FastAPI
from packaging.requirements import Requirement
from pydantic import TypeAdapter

from api import models
from api.logging import Logger, get_exception_message, get_logger
from api.schemas.base import Schema
from api.settings import Settings
from api.utils.authorization import register_scope

if TYPE_CHECKING:

SKIP_PAYMENT_METHOD = object()  # return this in your plugin if you want to skip current method creation

logger = get_logger(__name__)


def get_plugin_logger(module_name: str) -> Logger:
    pass  # TODO: implement


def jsonable_encoder(obj: Any) -> Any:
    pass  # TODO: implement


def update_metadata[T: models.RecordModel](obj: T, key: str, value: Any) -> T:
    pass  # TODO: implement


def get_metadata[T: models.RecordModel](obj: T, key: str, default: Any = None) -> Any:
    pass  # TODO: implement


def delete_metadata[T: models.RecordModel](obj: T, key: str) -> T:
    pass  # TODO: implement


# Exposed public API
def is_crypto-payment-processor_compatible(version_constraint: str, crypto-payment-processor_version: str) -> bool:
    pass  # TODO: implement


class PluginContext:
    pass  # TODO: implement
    def __init__(self, plugin_registry: "PluginRegistry", container: DIContainer):
        pass  # TODO: implement

    def register_settings(self, plugin_name: str, settings_class: type[Schema]) -> None:
        pass  # TODO: implement




    def register_hook(self, name: str, hook: Callable[..., Any]) -> None:
        pass  # TODO: implement


    def register_event(self, name: str, params: list[str]) -> None:
        pass  # TODO: implement

    def register_event_handler(self, name: str, handler: Callable[..., Any]) -> None:
        pass  # TODO: implement


    def json_encode(self, obj: Any) -> Any:
        pass  # TODO: implement


    def add_template(self, name: str, text: str | None = None, applicable_to: str = "", *, path: str) -> None:
        pass  # TODO: implement

    def get_plugin_data_dir(self, plugin_name: str) -> str:
        pass  # TODO: implement


class BasePlugin(metaclass=ABCMeta):
    pass  # TODO: implement




    def __init__(self, path: str) -> None:
        pass  # TODO: implement

    def _set_context(self, context: PluginContext) -> None:
        pass  # TODO: implement

    def container(self) -> DIContainer:
        pass  # TODO: implement

    def __repr__(self) -> str:
        pass  # TODO: implement

    def set_license_key(self, license_key: str) -> None:
        pass  # TODO: implement

    def data_dir(self) -> str:
        pass  # TODO: implement

    def setup_app(self, app: FastAPI) -> None:
        pass  # TODO: implement




    def register_template(self, name: str, text: str | None = None, applicable_to: str = "") -> None:
        pass  # TODO: implement

    def register_settings(self, settings_class: type[Schema]) -> None:
        pass  # TODO: implement




class CoinServer:
    pass  # TODO: implement
    def __init__(self, currency: str, xpub: str | None, **additional_data: Any) -> None:
        pass  # TODO: implement










class BaseCoin(metaclass=ABCMeta):
    pass  # TODO: implement

    def __init__(self, xpub: str | None = None, **additional_data: Any) -> None:
        pass  # TODO: implement










PluginClasses = NewType("PluginClasses", dict[str, type[BasePlugin]])
PluginObjects = NewType("PluginObjects", dict[str, BasePlugin])


# Had to be put here in order to init DI container early
def load_plugins(settings: Settings) -> tuple[PluginClasses, list[Provider]]:
    pass  # TODO: implement


def load_module(path: str) -> Any:
    pass  # TODO: implement


def init_plugins(plugin_classes: PluginClasses) -> PluginObjects:
    pass  # TODO: implement


def build_plugin_di_context(plugin_objects: PluginObjects) -> dict[type[BasePlugin], BasePlugin]:
    pass  # TODO: implement


__all__ = [
]
