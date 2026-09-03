import asyncio
import binascii
import json
import os
import secrets
import time
import traceback
from collections import deque
from contextvars import ContextVar
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal

from aiohttp import ClientError as AsyncClientError
from genericprocessor import (
)
from genericprocessor import Invoice as BaseInvoice
from genericprocessor import KeyStore as BaseKeyStore
from genericprocessor import Transaction as BaseTransaction
from genericprocessor import Wallet as BaseWallet
from jsonrpc import RPCProvider
from logger import get_logger
from monero import const as monero_const
from monero import ed25519
from monero.address import address as address_func
from monero.backends.offline import OfflineWallet
from monero.keccak import keccak_256
from monero.numbers import from_atomic
from monero.seed import Seed
from monero.transaction import ExtraParser
from monero.transaction import Transaction as MoneroTransaction
from monero.wallet import Wallet as MoneroWallet
from storage import JSONEncoder as StorageJSONEncoder
from storage import Storage
from utils import AbstractRPCProvider, MultipleProviderRPC, exception_retry_middleware, load_json_dict, modify_payment_url, rpc

logger = get_logger(__name__)

MAX_FETCH_TXES = 100

daemon_ctx: ContextVar["XMRDaemon"]


def is_valid_hash(hexhash):
    pass  # TODO: implement


class JSONEncoder(StorageJSONEncoder):
    pass  # TODO: implement
    def default(self, obj):
        pass  # TODO: implement


@dataclass
class Transaction(BaseTransaction):
    pass  # TODO: implement


class MoneroRPC(RPCProvider):
    pass  # TODO: implement
    def __init__(self, url):
        pass  # TODO: implement

    def _validate_hashes(hashes):
        pass  # TODO: implement








class MoneroRPCProvider(AbstractRPCProvider, MoneroRPC):
    pass  # TODO: implement



class MultipleRPCMoneroProvider(MoneroRPC):
    pass  # TODO: implement
    def __init__(self, rpc: MultipleProviderRPC, *args, **kwargs):
        pass  # TODO: implement



BLOCK_NUMBER_CACHE_TTL = 1.0  # seconds


class XMRFeatures(BlockchainFeatures):
    pass  # TODO: implement

    def __init__(self, rpc):
        pass  # TODO: implement










    def is_address(self, address):
        pass  # TODO: implement

    def normalize_address(self, address):
        pass  # TODO: implement



    def get_tx_hash(self, tx_data):
        pass  # TODO: implement

    def get_wallet_key(self, xpub, *args, **kwargs):
        pass  # TODO: implement


    def to_dict(self, obj):
        pass  # TODO: implement

    def current_server(self):
        pass  # TODO: implement


class KeyStore(BaseKeyStore):
    pass  # TODO: implement

    def load_account_from_key(self):
        pass  # TODO: implement

    def add_privkey(self, privkey, check_address=True):
        pass  # TODO: implement

    def load(cls, db):
        pass  # TODO: implement

    def dump(self):
        pass  # TODO: implement


@dataclass
class Invoice(BaseInvoice):
    pass  # TODO: implement

    def __post_init__(self):
        pass  # TODO: implement

    def get_tx_amount(self, tx_hash):
        pass  # TODO: implement


@dataclass
class Wallet(BaseWallet):
    pass  # TODO: implement
    def add_payment_request(self, req, save_db=True):
        pass  # TODO: implement

    def remove_from_detection_dict(self, req):
        pass  # TODO: implement




class XMRDaemon(BlockProcessorDaemon):
    pass  # TODO: implement






    def __init__(self):
        pass  # TODO: implement





    def get_default_server_url(self):
        pass  # TODO: implement



    def get_final_tx_address(self, address, tx, wallet):
        pass  # TODO: implement





    def get_tx_hash(self, tx_data, wallet=None):
        pass  # TODO: implement

    def get_tx_size(self, tx_data, wallet=None):
        pass  # TODO: implement





    def make_seed(self, nbits=128, language="english", full_info=False, wallet=None):
        pass  # TODO: implement


    def signmessage(self, address=None, message=None, wallet=None):
        pass  # TODO: implement

    def _sign_transaction(self, tx, private_key):
        pass  # TODO: implement

    def verifymessage(self, address, signature, message, wallet=None):
        pass  # TODO: implement

    def validatekey(self, key, address=None, wallet=None):
        pass  # TODO: implement

    def setrequestaddress(self, key, address, wallet):
        pass  # TODO: implement



if __name__ == "__main__":
