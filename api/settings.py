import fnmatch
import os
import re
from enum import StrEnum
from typing import Annotated

from pydantic import Field, PostgresDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

from api.constants import HTTPS_REVERSE_PROXIES


class Environment(StrEnum):
    pass  # TODO: implement


class Settings(BaseSettings):
    pass  # TODO: implement



















    def log_file(self) -> str | None:
        pass  # TODO: implement

    def log_file_regex(self) -> re.Pattern[str] | None:
        pass  # TODO: implement

    def logserver_client_host(self) -> str:
        pass  # TODO: implement

    def logserver_host(self) -> str:
        pass  # TODO: implement

    def redis_url(self) -> str:
        pass  # TODO: implement

    def validate_db_database(cls, v: str, info: ValidationInfo) -> str:
        pass  # TODO: implement

    def validate_enabled_cryptos(cls, v: str) -> CommaSeparatedStrings:
        pass  # TODO: implement

    def set_datadir(cls, path: str) -> str:
        pass  # TODO: implement


    def set_backups_dir(cls, path: str) -> str:
        pass  # TODO: implement


    def set_backend_plugins_dir(cls, path: str) -> str:
        pass  # TODO: implement


    def set_admin_plugins_dir(cls, path: str) -> str:
        pass  # TODO: implement


    def set_store_plugins_dir(cls, path: str) -> str:
        pass  # TODO: implement


    def set_docker_plugins_dir(cls, path: str) -> str:
        pass  # TODO: implement


    def images_dir(self) -> str:
        pass  # TODO: implement


    def products_image_dir(self) -> str:
        pass  # TODO: implement


    def files_dir(self) -> str:
        pass  # TODO: implement


    def log_dir(self) -> str:
        pass  # TODO: implement


    def plugins_dir(self) -> str:
        pass  # TODO: implement


    def get_plugin_data_dir(self, plugin_name: str) -> str:
        pass  # TODO: implement


    def build_postgres_dsn(self, db_name: str | None = None, driver: str = "asyncpg") -> str:
        pass  # TODO: implement

    def postgres_dsn(self) -> str:
        pass  # TODO: implement

    def protocol(self) -> str:
        pass  # TODO: implement

    def admin_url(self) -> str:
        pass  # TODO: implement

    def api_url(self) -> str:
        pass  # TODO: implement

    def coingecko_api_url(self) -> str:
        pass  # TODO: implement

    def coingecko_headers(self) -> dict[str, str]:
        pass  # TODO: implement

    def is_environment(self, environments: set[Environment]) -> bool:
        pass  # TODO: implement

    def is_development(self) -> bool:
        pass  # TODO: implement

    def is_testing(self) -> bool:
        pass  # TODO: implement

    def is_sandbox(self) -> bool:
        pass  # TODO: implement

    def is_production(self) -> bool:
        pass  # TODO: implement
