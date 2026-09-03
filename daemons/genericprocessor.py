from base import BaseDaemon  # isort: skip

import asyncio
import functools
import inspect
import json
import os
import secrets
import time
import traceback
from abc import ABCMeta, abstractmethod
from collections import defaultdict, deque
from contextvars import ContextVar
from dataclasses import dataclass, field
from decimal import Decimal

from aiohttp import ClientSession
from logger import get_logger
from storage import ConfigDB as StorageConfigDB
from storage import JSONEncoder as StorageJSONEncoder
from storage import Storage, StoredDBProperty, StoredObject, StoredProperty, decimal_to_string
from storage import WalletDB as StorageWalletDB
from utils import CastingDataclass, JsonResponse, get_exception_message, get_function_header, hide_logging_errors, rpc

logger = get_logger(__name__)

NO_HISTORY_MESSAGE = "We don't access transaction history to remain lightweight"
WRITE_DOWN_SEED_MESSAGE = "Please keep your seed in a safe place; if you lose it, you will not be able to restore your wallet."
ONE_ADDRESS_MESSAGE = "We only support one address per wallet because of current blockchain specifics"
GET_PROOF_MESSAGE = "Currrent blockchain doesn't support get_proof correctly for now"
NO_MASTER_KEYS_MESSAGE = "As we use only one address per wallet, address keys are used, but not the xprv/xpub"


NOOP_PATH = object()

CHUNK_SIZE = 30
AMOUNTGEN_LIMIT = 10**9


# statuses of payment requests
PR_UNPAID = 0  # invoice amt not reached by txs in mempool+chain.
PR_EXPIRED = 1  # invoice is unpaid and expiry time reached
PR_PAID = 3  # paid and mined (1 conf).
PR_UNCONFIRMED = 7

daemon_ctx: ContextVar[BaseDaemon] = ContextVar("daemon")


@dataclass
class Transaction:
    pass  # TODO: implement


class BlockchainFeatures(metaclass=ABCMeta):
    pass  # TODO: implement
    def __init__(self, rpc):
        pass  # TODO: implement

    def get_block_number(self) -> int:
        pass  # TODO: implement


    def get_transaction(self, tx) -> dict:
        pass  # TODO: implement

    def get_tx_receipt(self, tx) -> dict:
        pass  # TODO: implement


    def get_balance(self, address) -> Decimal:
        pass  # TODO: implement

    def get_block(self, block, *args, **kwargs) -> dict:
        pass  # TODO: implement


    def is_address(self, address) -> bool:
        pass  # TODO: implement

    def normalize_address(self, address) -> str:
        pass  # TODO: implement




    def get_tx_hash(self, tx_data) -> str:
        pass  # TODO: implement

    def get_gas_price(self) -> int:
        pass  # TODO: implement


    def get_wallet_key(self, xpub, *args, **kwargs):
        pass  # TODO: implement

    def to_dict(self, obj):
        pass  # TODO: implement

    def current_server(self):
        pass  # TODO: implement


pr_tooltips = {PR_UNPAID: "Unpaid", PR_PAID: "Paid", PR_EXPIRED: "Expired", PR_UNCONFIRMED: "Unconfirmed"}


STR_TO_BOOL_MAPPING = {
}  # common str -> bool conversions

# storage


class WalletDB(StorageWalletDB):
    pass  # TODO: implement

    def _convert_dict(self, path, key, v):
        pass  # TODO: implement

    def _should_convert_to_stored_dict(self, key) -> bool:
        pass  # TODO: implement

    def run_upgrades(self):
        pass  # TODO: implement

    def _convert_version_2(self):
        pass  # TODO: implement

    def _convert_version_3(self):
        pass  # TODO: implement

    def _convert_version_4(self):
        pass  # TODO: implement


class ConfigDB(StorageConfigDB):
    pass  # TODO: implement


def str_to_bool(s):
    pass  # TODO: implement



def get_exception_traceback(exc):
    pass  # TODO: implement


def from_wei(value: int, precision=None) -> Decimal:
    pass  # TODO: implement


def to_wei(value: Decimal, precision=None) -> int:
    pass  # TODO: implement


@dataclass
class KeyStore(metaclass=ABCMeta):
    pass  # TODO: implement

    def is_watching_only(self):
        pass  # TODO: implement

    def __post_init__(self):
        pass  # TODO: implement

    def load_account_from_key(self):
        pass  # TODO: implement

    def add_privkey(self, privkey):
        pass  # TODO: implement

    def has_seed(self):
        pass  # TODO: implement

    def load(cls, db):
        pass  # TODO: implement

    def dump(self):
        pass  # TODO: implement


@dataclass
class Invoice(CastingDataclass, StoredObject):
    pass  # TODO: implement

    def __post_init__(self):
        pass  # TODO: implement

    def get_tx_amount(self, tx_hash):
        pass  # TODO: implement

    def export_tx_amounts(self, divisibility):
        pass  # TODO: implement

    def status_str(self):
        pass  # TODO: implement


@dataclass
class Wallet:
    pass  # TODO: implement


    def __post_init__(self):
        pass  # TODO: implement

    def save_db(self):
        pass  # TODO: implement






    def clear_requests(self):
        pass  # TODO: implement

    def is_synchronized(self):
        pass  # TODO: implement

    def is_watching_only(self):
        pass  # TODO: implement

    def get_private_key(self):
        pass  # TODO: implement

    def import_private_key(self, privkey):
        pass  # TODO: implement

    def address(self):
        pass  # TODO: implement

    def contract_addr(self):
        pass  # TODO: implement

    def wallet_key(self):
        pass  # TODO: implement


    def stop(self, block_number):
        pass  # TODO: implement



    def add_payment_request(self, req, save_db=True):
        pass  # TODO: implement



    def get_request(self, key):
        pass  # TODO: implement

    def remove_from_detection_dict(self, req):
        pass  # TODO: implement

    def remove_request(self, key):
        pass  # TODO: implement

    def get_sorted_requests(self):
        pass  # TODO: implement

    def set_request_status(self, key, status, tx_hash=None, **kwargs):
        pass  # TODO: implement

    def set_request_address(self, key, address):
        pass  # TODO: implement





class BlockProcessorDaemon(BaseDaemon, metaclass=ABCMeta):
    pass  # TODO: implement








    def __init__(self):
        pass  # TODO: implement




    def get_default_server_url(self):
        pass  # TODO: implement

    def load_env(self):
        pass  # TODO: implement











    def get_method_data(self, method):
        pass  # TODO: implement

    def get_exception_message(self, e):
        pass  # TODO: implement

    def user_dir(self):
        pass  # TODO: implement

    def get_datadir(self):
        pass  # TODO: implement

    def get_wallet_path(self):
        pass  # TODO: implement













    def clear_requests(self, wallet):
        pass  # TODO: implement







    def get_tx_hash(self, tx_data, wallet=None):
        pass  # TODO: implement

    def get_tx_size(self, tx_data, wallet=None):
        pass  # TODO: implement


    def get_updates(self, wallet):
        pass  # TODO: implement


    def getaddress(self, wallet):
        pass  # TODO: implement


    def getaddresshistory(self, *args, **kwargs):
        pass  # TODO: implement


    def getconfig(self, key, wallet=None):
        pass  # TODO: implement




    def getmasterprivate(self, *args, **kwargs):
        pass  # TODO: implement

    def getmerkle(self, *args, **kwargs):
        pass  # TODO: implement

    def getmpk(self, *args, **kwargs):
        pass  # TODO: implement

    def getprivatekeys(self, *args, wallet=None):
        pass  # TODO: implement

    def getpubkeys(self, *args, wallet=None):
        pass  # TODO: implement


    def getseed(self, *args, wallet=None):
        pass  # TODO: implement

    def getservers(self, wallet=None):
        pass  # TODO: implement


    def help(self, func=None, wallet=None):
        pass  # TODO: implement


    def importprivkey(self, privkey, wallet):
        pass  # TODO: implement

    def is_synchronized(self, wallet):
        pass  # TODO: implement

    def ismine(self, address, wallet):
        pass  # TODO: implement



    def list_wallets(self, wallet=None):
        pass  # TODO: implement


    def make_seed(self, nbits=128, language="english", full_info=False, wallet=None):
        pass  # TODO: implement

    def normalizeaddress(self, address, wallet=None):
        pass  # TODO: implement



    def removelocaltx(self, *args, **kwargs):
        pass  # TODO: implement


    def restore_wallet_from_text(self, text, contract=None, path=None, address=None, **kwargs):
        pass  # TODO: implement

    def restore(self, text, wallet=None, wallet_path=None, contract=None, address=None, **kwargs):
        pass  # TODO: implement

    def rmrequest(self, key, wallet):
        pass  # TODO: implement


    def setrequestaddress(self, key, address, wallet):
        pass  # TODO: implement

    def signmessage(self, address=None, message=None, wallet=None):
        pass  # TODO: implement

    def _sign_transaction(self, tx, private_key):
        pass  # TODO: implement

    def signtransaction(self, tx, wallet=None):
        pass  # TODO: implement

    def signtransaction_with_privkey(self, tx, privkey, wallet=None):
        pass  # TODO: implement

    def validateaddress(self, address, wallet=None):
        pass  # TODO: implement

    def validatekey(self, key, wallet=None, **kwargs):
        pass  # TODO: implement

    def version(self, wallet=None):
        pass  # TODO: implement


    def validatecontract(self, address, wallet=None):
        pass  # TODO: implement

    def get_tokens(self, wallet=None):
        pass  # TODO: implement

    def getabi(self, wallet=None):
        pass  # TODO: implement

    def debuglocks(self, wallet=None):
        pass  # TODO: implement
