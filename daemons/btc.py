from base import BaseDaemon  # isort: skip

import argparse
import asyncio
import contextlib
import functools
import inspect
import os
import sys
import traceback
from collections import deque
from decimal import Decimal
from types import ModuleType
from urllib.parse import urlparse

from logger import configure_logging, get_logger
from utils import (
)

logger = get_logger(__name__)


class BTCDaemon(BaseDaemon):
    pass  # TODO: implement


    def register_aliases(self):
        pass  # TODO: implement

    def load_electrum(self):
        pass  # TODO: implement


    def __init__(self):
        pass  # TODO: implement

    def load_env(self):
        pass  # TODO: implement

    def _serialize_proxy(self, proxy_dict):
        pass  # TODO: implement

    def get_proxy_settings(self):
        pass  # TODO: implement

    def set_dynamic_spec(self):
        pass  # TODO: implement

    def available_events(self):
        pass  # TODO: implement

    def config_options(self):
        pass  # TODO: implement

    def create_config(self):
        pass  # TODO: implement

    def setup_config_and_logging(self):
        pass  # TODO: implement

    def configure_logging(self, electrum_config):
        pass  # TODO: implement

    def create_daemon(self):
        pass  # TODO: implement

    def register_callbacks(self, callback_function):
        pass  # TODO: implement




    def create_commands(self, config):
        pass  # TODO: implement


    def load_cmd_wallet(self, cmd, wallet):
        pass  # TODO: implement

    def create_wallet(self, storage, config):
        pass  # TODO: implement

    def init_wallet(self, wallet):
        pass  # TODO: implement

    def copy_config_settings(self, config):
        pass  # TODO: implement

    def is_still_syncing(self, wallet=None):
        pass  # TODO: implement





    def add_wallet_to_command(self, wallet, req_method, exec_method, **kwargs):
        pass  # TODO: implement

    def get_method_data(self, method, custom):
        pass  # TODO: implement




    def get_exception_message(self, e):
        pass  # TODO: implement

    def get_wallet_key(self, xpub, contract=None, **extra_params):
        pass  # TODO: implement


    def _find_matching_wallet_key(self, wallet):
        pass  # TODO: implement


    def _process_events_sync(self, event, *args):
        pass  # TODO: implement

    def process_new_block(self):
        pass  # TODO: implement

    def process_new_transaction(self, args):
        pass  # TODO: implement

    def process_verified_tx(self, args):
        pass  # TODO: implement

    def get_status_str(self, status):
        pass  # TODO: implement

    def _get_request(self, wallet, address):
        pass  # TODO: implement

    def _get_request_address(self, invoice):
        pass  # TODO: implement

    def get_tx_hashes_for_invoice(self, wallet, invoice):
        pass  # TODO: implement

    def is_paid_via_lightning(self, wallet, invoice):
        pass  # TODO: implement

    def format_satoshis(self, x, wallet=None):
        pass  # TODO: implement

    def process_new_payment(self, wallet, request_id, status):
        pass  # TODO: implement

    def process_events(self, event, *args):
        pass  # TODO: implement

    def get_tx_amounts(self, wallet, address, tx_hashes, request):
        pass  # TODO: implement

    def get_payment_amounts(self, wallet, address, tx_hashes, request):
        pass  # TODO: implement


    def validatekey(self, key, wallet=None):
        pass  # TODO: implement

    def get_updates(self, wallet):
        pass  # TODO: implement





    def get_tx_size(self, raw_tx: dict, wallet=None) -> int:
        pass  # TODO: implement

    def get_tx_hash(self, raw_tx: dict, wallet=None) -> int:
        pass  # TODO: implement

    def get_default_fee(self, tx: str | int, wallet=None) -> float:
        pass  # TODO: implement

    def recommended_fee(self, target, wallet=None) -> float:
        pass  # TODO: implement

    def get_invoice(self, key, wallet):
        pass  # TODO: implement

    def get_address_balance(self, address, wallet):
        pass  # TODO: implement

    def getaddressbalance_wallet(self, address, wallet):
        pass  # TODO: implement

    def validatecontract(self, address, wallet=None):  # fallback for other coins without smart contracts
        pass  # TODO: implement

    def get_tokens(self, wallet=None):  # fallback
        pass  # TODO: implement

    def getabi(self, wallet=None):  # fallback
        pass  # TODO: implement

    def normalizeaddress(self, address, wallet=None):  # fallback
        pass  # TODO: implement

    def setrequestaddress(self, key, address, wallet):
        pass  # TODO: implement












if __name__ == "__main__":
