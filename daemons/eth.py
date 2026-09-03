import asyncio
import contextlib
import json
import os
import traceback
from collections import deque, namedtuple
from contextvars import ContextVar
from dataclasses import dataclass
from decimal import Decimal
from typing import Any

from aiohttp import ClientError as AsyncClientError
from aiolimiter import AsyncLimiter
from eth_account import Account
from eth_account.messages import encode_defunct
from eth_keys.datatypes import PrivateKey, PublicKey
from genericprocessor import (
)
from genericprocessor import KeyStore as BaseKeyStore
from genericprocessor import Wallet as BaseWallet
from hexbytes import HexBytes
from logger import get_logger
from mnemonic import Mnemonic
from storage import JSONEncoder as StorageJSONEncoder
from storage import Storage, decimal_to_string
from utils import (
)
from web3 import AsyncWeb3
from web3._utils.events import get_event_data
from web3._utils.rpc_abi import RPC as ETHRPC
from web3.contract import AsyncContract
from web3.datastructures import AttributeDict
from web3.exceptions import ABIFunctionNotFound, BlockNotFound, TransactionNotFound, Web3Exception
from web3.middleware import ExtraDataToPOAMiddleware, Web3Middleware
from web3.middleware.base import MiddlewareOnion
from web3.providers.rpc.async_rpc import HTTPSessionManager
from web3.types import RPCEndpoint, RPCResponse

logger = get_logger(__name__)

Account.enable_unaudited_hdwallet_features()

daemon_ctx: ContextVar["ETHDaemon"]

EIP1559_PARAMS = ("maxFeePerGas", "maxPriorityFeePerGas")
FEE_PARAMS = EIP1559_PARAMS + ("gasPrice", "gas")

TX_DEFAULT_GAS = 21000

RPC_SOURCE = "Infura"

TRANSFER_TOPIC = AsyncWeb3.keccak(text="Transfer(address,address,uint256)").to_0x_hex()


class JSONEncoder(StorageJSONEncoder):
    pass  # TODO: implement
    def default(self, obj):
        pass  # TODO: implement


class MultipleRPCEthereumProvider(AsyncWeb3.AsyncHTTPProvider):
    pass  # TODO: implement
    def __init__(self, rpc: MultipleProviderRPC, *args, **kwargs):
        pass  # TODO: implement



class EthereumRPCProvider(AbstractRPCProvider, AsyncWeb3.AsyncHTTPProvider):
    pass  # TODO: implement





class ETHFeatures(BlockchainFeatures):
    pass  # TODO: implement

    def __init__(self, web3):
        pass  # TODO: implement











    def is_address(self, address):
        pass  # TODO: implement

    def normalize_address(self, address):
        pass  # TODO: implement




    def find_all_trace_outputs(self, debug_data):
        pass  # TODO: implement

    def _find_all_trace_tx_outputs_geth(self, tx_hash, from_addr, debug_data, depth=0):
        pass  # TODO: implement

    def _find_all_trace_outputs_geth(self, debug_data):
        pass  # TODO: implement

    def get_tx_hash(self, tx_data):
        pass  # TODO: implement

    def to_dict(self, obj):
        pass  # TODO: implement

    def get_wallet_key(self, xpub, contract=None, **extra_params):
        pass  # TODO: implement


    def current_server(self):
        pass  # TODO: implement


with open("daemons/abi/erc20.json") as f:

with open("daemons/tokens/erc20.json") as f:


# NOTE: there are 2 types of retry middlewares installed
# This middleware handles network error and unexpected RPC failures
# For BlockNotFound and TransactionNotFound we create _safe variants where needed
class AsyncHTTPRetryMiddleware(Web3Middleware):
    pass  # TODO: implement


RPC_ORIGIN = "metamask"
RPC_DEST = "internal"


@dataclass
class KeyStore(BaseKeyStore):
    pass  # TODO: implement

    def load_contract(self):
        pass  # TODO: implement

    def __post_init__(self):
        pass  # TODO: implement

    def load_account_from_key(self):
        pass  # TODO: implement

    def add_privkey(self, privkey):
        pass  # TODO: implement

    def load(cls, db):
        pass  # TODO: implement

    def dump(self):
        pass  # TODO: implement


@dataclass
class Wallet(BaseWallet):
    pass  # TODO: implement

    def contract_addr(self):
        pass  # TODO: implement





TransferEventParams = namedtuple("TransferEventParams", ["abi", "from_addr", "to", "value"])


class ETHDaemon(BlockProcessorDaemon):
    pass  # TODO: implement








    def __init__(self):
        pass  # TODO: implement

    def parse_transfer_event_abi(self):
        pass  # TODO: implement



    def load_env(self):
        pass  # TODO: implement





    def get_default_server_url(self):
        pass  # TODO: implement



    def _process_param(self, wallet, extra_params, key):
        pass  # TODO: implement

    def process_extra_params(self, wallet, extra_params):
        pass  # TODO: implement








    def get_tokens(self, wallet=None):
        pass  # TODO: implement

    def get_tx_hash(self, tx_data, wallet=None):
        pass  # TODO: implement

    def get_tx_size(self, tx_data, wallet=None):
        pass  # TODO: implement


    def getabi(self, wallet=None):
        pass  # TODO: implement




    def make_seed(self, nbits=128, language="english", full_info=False, wallet=None):
        pass  # TODO: implement





    def _get_contract_cache_key(self, address):
        pass  # TODO: implement


    def signmessage(self, address=None, message=None, wallet=None):
        pass  # TODO: implement

    def _sign_transaction(self, tx, private_key):
        pass  # TODO: implement



    def verifymessage(self, address, signature, message, wallet=None):
        pass  # TODO: implement




if __name__ == "__main__":
