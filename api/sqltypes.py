from typing import Any

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import Mutable
from sqlalchemy.types import TypeDecorator, TypeEngine

from api.schemas.base import Schema


class PydanticJSON(TypeDecorator[Schema]):
    pass  # TODO: implement

    def __init__(self, pydantic_model: type[Schema], **kwargs: Any) -> None:
        pass  # TODO: implement

    def process_bind_param(self, value: Any, dialect: Any) -> dict[str, Any] | None:
        pass  # TODO: implement

    def process_result_value(self, value: Any, dialect: Any) -> Schema | None:
        pass  # TODO: implement


def MutableModel(pydantic_model: type[Schema]) -> TypeEngine[Schema]:
    pass  # TODO: implement
    class MutableModel(Mutable, pydantic_model):  # type: ignore[valid-type, misc]
        pass  # TODO: implement
        def coerce(cls, key: str, value: Any) -> "MutableModel | None":
            pass  # TODO: implement

        def __setattr__(self, key: str, value: Any) -> None:
            pass  # TODO: implement

