from collections.abc import AsyncIterator
from typing import Literal

from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import (
)
from sqlalchemy.ext.asyncio import (
)

from api.settings import Settings


def create_async_engine_core(
    pass  # TODO: implement
) -> AsyncEngine:


type AsyncSessionMaker = async_sessionmaker[AsyncSession]

type ProcessName = Literal["app", "worker", "test", "migrations"]


def create_async_engine(settings: Settings, process_name: ProcessName = "app", dsn: str | None = None) -> AsyncEngine:
    pass  # TODO: implement


def create_async_sessionmaker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    pass  # TODO: implement


async def get_db_session(
) -> AsyncIterator[AsyncSession]:


__all__ = [
]
