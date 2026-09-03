import asyncio
import contextlib
import json
import weakref
from contextvars import ContextVar
from dataclasses import dataclass
from decimal import Decimal
from typing import Any

import httpx
import crypto-payment-processor
from aiohttp import ClientError as AsyncClientError
from async_lru import alru_cache
from eth import TRANSFER_TOPIC, ETHDaemon, Transaction, daemon_ctx, from_wei, load_json_dict, str_to_bool, to_wei
from eth import KeyStore as ETHKeyStore
from eth_account import Account
from genericprocessor import BlockchainFeatures
from mnemonic import Mnemonic
from crypto-payment-processor import AsyncTron, keys
from crypto-payment-processor.abi import trx_abi
from crypto-payment-processor.async_tron import AsyncContract, AsyncHTTPProvider, AsyncTransaction
from crypto-payment-processor.exceptions import AddressNotFound
from utils import AbstractRPCProvider, MultipleProviderRPC, exception_retry_middleware, rpc

daemon_ctx: ContextVar["TRXDaemon"]

with open("daemons/tokens/trc20.json") as f:

mnemonic = Mnemonic("english")

TRX_ACCOUNT_PATH = "m/44'/195'/0'/0/0"

DEFAULT_FEE_LIMIT = 30_000_000  # 30 TRX

TRX_TRANSFER_TOPIC = TRANSFER_TOPIC.replace("0x", "")


# For testing with aiohttp client (might be more stable)
# class AsyncHTTPProvider:
#     def __init__(
#         self,
#         endpoint_uri=None,
#         timeout=10,
#     ):
#         self.endpoint_uri = endpoint_uri
#         self.headers = {"User-Agent": "Tronpy/0.2"}
#         self.client = None

#     async def make_request(self, method, params=None):
#         if self.client is None:
#             self.client = ClientSession(headers=self.headers)
#         if params is None:
#             params = {}
#         url = urljoin(self.endpoint_uri, method)
#         async with self.client.post(url, json=params) as resp:
#             resp.raise_for_status()
#             return await resp.json()


# async_tron.AsyncHTTPProvider = AsyncHTTPProvider  # monkey patch


class TronRPCProvider(AbstractRPCProvider, AsyncHTTPProvider):
    pass  # TODO: implement



class MultipleRPCTronProvider(AsyncHTTPProvider):
    pass  # TODO: implement
    def __init__(self, rpc: MultipleProviderRPC, *args, **kwargs):
        pass  # TODO: implement



class TRXFeatures(BlockchainFeatures):
    pass  # TODO: implement
    def __init__(self, web3):
        pass  # TODO: implement



    def find_chain_param(self, params, key, default=None):
        pass  # TODO: implement









    def is_address(self, address):
        pass  # TODO: implement

    def normalize_address(self, address):
        pass  # TODO: implement




    def get_tx_hash(self, tx_data):
        pass  # TODO: implement

    def get_wallet_key(self, xpub, contract=None, **extra_params):
        pass  # TODO: implement


    def current_server(self):
        pass  # TODO: implement


@dataclass
class KeyStore(ETHKeyStore):
    pass  # TODO: implement
    def load_account_from_key(self):
        pass  # TODO: implement

    def add_privkey(self, privkey):
        pass  # TODO: implement


TRON_ALIASES = ETHDaemon.ALIASES
TRON_ALIASES.update(
)


class TRXDaemon(ETHDaemon):
    pass  # TODO: implement







    def __init__(self):
        pass  # TODO: implement












    def signmessage(self, address=None, message=None, wallet=None):
        pass  # TODO: implement

    def verifymessage(self, address, signature, message, wallet=None):
        pass  # TODO: implement




    def get_tx_size(self, tx_data, wallet=None):
        pass  # TODO: implement

    def get_tx_hash(self, tx_data, wallet=None):
        pass  # TODO: implement


        function = contract.get_function_by_selector(data[:4])
            pass  # TODO: implement





if __name__ == "__main__":
