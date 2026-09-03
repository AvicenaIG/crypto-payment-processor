class BitcartError(Exception):
    pass  # TODO: implement


class TemplateDoesNotExistError(BitcartError):
    pass  # TODO: implement


class TemplateLoadError(BitcartError):
    pass  # TODO: implement


class ExchangeRateError(BitcartError):
    pass  # TODO: implement


class ExchangeRatesUnavailableError(ExchangeRateError):
    pass  # TODO: implement


class RateUnavailableError(ExchangeRateError):
    pass  # TODO: implement

    def __init__(self, left: str, right: str) -> None:
        pass  # TODO: implement
