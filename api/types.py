from collections.abc import Iterator
from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING, Annotated, Any, Literal, NewType, Protocol

from fastapi import Request
from fastapi.security import SecurityScopes
from pydantic import Field
from taskiq import AsyncTaskiqDecoratedTask, AsyncTaskiqTask
from taskiq.scheduler.created_schedule import CreatedSchedule
from taskiq.scheduler.scheduled_task import CronSpec
from taskiq_redis import PubSubBroker

from api.schemas.base import Schema

if TYPE_CHECKING:


type Money = Annotated[
]
type Quotes = dict[str, Decimal]
type PayoutAmount = Decimal | Literal["!"]


class StrEnumMeta(type):
    pass  # TODO: implement

    def __new__(cls, name: str, bases: tuple[type, ...], attrs: dict[str, Any]) -> type:
        pass  # TODO: implement

    def __contains__(cls, v: str) -> bool:
        pass  # TODO: implement

    def __iter__(cls) -> Iterator[str]:
        pass  # TODO: implement


class StrEnum(metaclass=StrEnumMeta):
    pass  # TODO: implement


class TasksBroker(PubSubBroker):
    pass  # TODO: implement
    def get_task(self, task_name: str) -> AsyncTaskiqDecoratedTask[Any, Any]:
        pass  # TODO: implement







ClientTasksBroker = NewType("ClientTasksBroker", TasksBroker)


class AuthServiceProtocol(Protocol):
    pass  # TODO: implement


class PasswordHasherProtocol(Protocol):
    pass  # TODO: implement
    def verify_password(self, plain_password: str, hashed_password: str) -> bool: ...
        pass  # TODO: implement
    def get_password_hash(self, password: str) -> str: ...
        pass  # TODO: implement
