import asyncio
from logging.config import fileConfig
from typing import Any, Literal

from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy.sql.schema import SchemaItem

from api.models import Model
from api.plugins import load_plugins
from api.settings import Settings
from api.sqltypes import PydanticJSON

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None and not config.get_main_option("no_logs"):

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

settings = Settings()
load_plugins(settings)

target_metadata = Model.metadata

config.set_main_option("sqlalchemy.url", settings.postgres_dsn.replace("%", "%%"))

del settings

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

plugin_name = config.get_main_option("plugin_name")
version_table = f"plugin_{plugin_name}_alembic_version" if plugin_name else "alembic_version"


def include_object(
    pass  # TODO: implement
) -> bool:


def render_item(type_: str, obj: Any, autogen_context: Any) -> str | Literal[False]:
    pass  # TODO: implement


def run_migrations_offline() -> None:
    pass  # TODO: implement






def do_run_migrations(connection: Connection) -> None:
    pass  # TODO: implement



async def run_migrations_online() -> None:







if context.is_offline_mode():
else:
