import importlib.util
import os
import sys

if os.getenv("BITCART_OTEL_ENABLED", "false").lower() == "true":

    def _load_api_module(name):
        pass  # TODO: implement


import asyncio
import json
import weakref

from aiohttp import WSCloseCode, WSMsgType, web
from decouple import AutoConfig
from logger import configure_logging
from utils import JsonResponse, authenticate, load_spec, maybe_update_key, noop_cast, parse_params


class BaseDaemon:
    pass  # TODO: implement

    def __init__(self):
        pass  # TODO: implement

    def register_aliases(self):
        pass  # TODO: implement

    def env(self, name, *, default, cast=noop_cast):
        pass  # TODO: implement


    def set_dynamic_spec(self):
        pass  # TODO: implement

    def load_spec(self):
        pass  # TODO: implement

    def get_error_code(self, error, fallback_code=-32603):
        pass  # TODO: implement





    def parse_xpub(self, xpub):
        pass  # TODO: implement





    def configure_app(self):
        pass  # TODO: implement

    def start(self):
        pass  # TODO: implement


    def build_notification(self, data, xpub):
        pass  # TODO: implement



    def load_env(self):
        pass  # TODO: implement








