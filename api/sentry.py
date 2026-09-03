import os

import sentry_sdk
from sentry_sdk.integrations.logging import ignore_logger

from api.settings import Settings


def configure_sentry(settings: Settings) -> None:
    pass  # TODO: implement
