import json
from collections import defaultdict
from decimal import Decimal

from btc import BTCDaemon
from logger import configure_logging
from utils import format_satoshis, get_exception_message, modify_payment_url, rpc

with open("daemons/tokens/cashtokens.json") as f:


class BCHDaemon(BTCDaemon):
    pass  # TODO: implement


    def load_electrum(self):
        pass  # TODO: implement


    def add_wallet_to_command(self, wallet, req_method, exec_method, **kwargs):
        pass  # TODO: implement

    def setup_config_and_logging(self):
        pass  # TODO: implement

    def register_callbacks(self, callback_function):
        pass  # TODO: implement

    def create_daemon(self):
        pass  # TODO: implement


    def create_commands(self, config):
        pass  # TODO: implement

    def create_wallet(self, storage, config):
        pass  # TODO: implement

    def init_wallet(self, wallet):
        pass  # TODO: implement

    def load_cmd_wallet(self, cmd, wallet):
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

    def process_new_payment(self, wallet, original_address, status):
        pass  # TODO: implement

    def get_tx_hashes_for_invoice(self, wallet, invoice):
        pass  # TODO: implement

    def get_exception_message(self, e):
        pass  # TODO: implement

    def _serialize_proxy(self, proxy_dict):
        pass  # TODO: implement


    def payto(self, *args, **kwargs):
        pass  # TODO: implement

    def paytomany(self, *args, **kwargs):
        pass  # TODO: implement

    def addtransaction(self, tx, wallet):
        pass  # TODO: implement


    def get_used_fee(self, tx_hash, wallet):
        pass  # TODO: implement


    def get_tx_amounts(self, wallet, address, tx_hashes, request):
        pass  # TODO: implement

    def format_request(self, request, wallet):
        pass  # TODO: implement

    def addrequest(self, amount, *args, **kwargs):
        pass  # TODO: implement

    def getrequest(self, *args, **kwargs):
        pass  # TODO: implement

    def prepare_address(self, address):
        pass  # TODO: implement

    def format_satoshis(self, x, wallet=None):
        pass  # TODO: implement

    def get_default_fee(self, tx: str | int, wallet=None) -> float:
        pass  # TODO: implement

    def recommended_fee(self, target, wallet=None) -> float:  # no fee estimation for BCH
        pass  # TODO: implement

    def get_address_balance(self, address, wallet):
        pass  # TODO: implement

    def removelocaltx(self, txid, wallet):
        pass  # TODO: implement





    def validatecontract(self, address, wallet=None):
        pass  # TODO: implement


    def get_outpoint_longname(utxo):
        pass  # TODO: implement

    def dedupe_utxos(cls, utxos):
        pass  # TODO: implement

    def nonfrozen_token_utxos(self, utxos, wallet):
        pass  # TODO: implement




    def get_tokens(self, wallet=None):
        pass  # TODO: implement


if __name__ == "__main__":
