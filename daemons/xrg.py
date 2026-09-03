from bch import BCHDaemon
from utils import rpc


class XRGDaemon(BCHDaemon):
    pass  # TODO: implement

    def load_electrum(self):
        pass  # TODO: implement


    def addrequest(self, *args, **kwargs):
        pass  # TODO: implement

    def validatecontract(self, address, wallet=None):  # fallback for other coins without smart contracts
        pass  # TODO: implement

    def get_tokens(self, wallet=None):  # fallback
        pass  # TODO: implement


if __name__ == "__main__":
