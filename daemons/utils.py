import asyncio
import dataclasses
import inspect
import json
import logging
import sys
import time
import traceback
from abc import ABCMeta, abstractmethod
from base64 import b64decode
from contextlib import contextmanager
from dataclasses import dataclass
from decimal import Decimal
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from aiohttp import web
from logger import get_logger

logger = get_logger(__name__)


def noop_cast(v):
    pass  # TODO: implement


def format_satoshis(x, decimal_point=8):
    pass  # TODO: implement


def load_spec(spec_file, exit_on_error=True):
    pass  # TODO: implement


def maybe_update_key(dest, other, key):
    pass  # TODO: implement


def rpc(f=None, requires_wallet=False, requires_network=False, requires_lightning=False):
    pass  # TODO: implement
    def wrapper(f):
        pass  # TODO: implement



def authenticate(f):
    pass  # TODO: implement



def cached(f):
    pass  # TODO: implement
    def wrapper(*args, **kwargs):
        pass  # TODO: implement



def decode_auth(authstr):
    pass  # TODO: implement


def parse_params(params):
    pass  # TODO: implement


def get_exception_message(e):
    pass  # TODO: implement


@contextmanager
def hide_logging_errors(enable):
    pass  # TODO: implement


@dataclass
class JsonResponse:
    pass  # TODO: implement

    def send(self):
        pass  # TODO: implement

    def send_error_response(self):
        pass  # TODO: implement

    def send_ok_response(self):
        pass  # TODO: implement


async def periodic_task(self, process_func, interval):


class CastingDataclass:
    pass  # TODO: implement
    def __post_init__(self):
        pass  # TODO: implement


def load_json_dict(s, error_message):
    pass  # TODO: implement


def is_int(v):
    pass  # TODO: implement


def try_cast_num(v):
    pass  # TODO: implement


def get_func_name(func):
    pass  # TODO: implement
        func = func.__wrapped__
            pass  # TODO: implement


def exception_retry_middleware(make_request, errors, retries=5):
    pass  # TODO: implement



def async_partial(async_fn, *wrap_args):
    pass  # TODO: implement



def get_function_header(func, func_obj):
    pass  # TODO: implement


def modify_payment_url(key, url, amount):
    pass  # TODO: implement


class AbstractRPCProvider(metaclass=ABCMeta):
    pass  # TODO: implement



class MultipleProviderRPC(metaclass=ABCMeta):
    pass  # TODO: implement



    def __init__(self, providers: list[AbstractRPCProvider]):
        pass  # TODO: implement

    def current_rpc(self):
        pass  # TODO: implement

    def prev_rpc_idx(self, idx):
        pass  # TODO: implement

    def next_rpc_idx(self, idx):
        pass  # TODO: implement



    def is_last_rpc(self):
        pass  # TODO: implement





