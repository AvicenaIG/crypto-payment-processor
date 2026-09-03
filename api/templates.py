import re
from collections import defaultdict
from typing import Any

from jinja2 import TemplateError, Undefined
from jinja2.sandbox import SandboxedEnvironment

from api.exceptions import TemplateLoadError
from api.ext.moneyformat import currency_table
from api.logging import get_exception_message, get_logger
from api.plugins import delete_metadata, get_metadata, update_metadata

TG_MD_V1_RE = re.compile(r"[_*`\[]")

logger = get_logger(__name__)


def format_decimal(obj: Any, key: str, **kwargs: Any) -> Any:
    pass  # TODO: implement


def tg_escape(text: Any) -> str:
    pass  # TODO: implement


sandbox = SandboxedEnvironment(trim_blocks=True)
sandbox.filters["format_decimal"] = format_decimal
sandbox.filters["tg_escape"] = tg_escape
sandbox.globals["get_metadata"] = get_metadata
sandbox.globals["update_metadata"] = update_metadata
sandbox.globals["delete_metadata"] = delete_metadata


class Template:
    pass  # TODO: implement
    def __init__(self, name: str, text: str | None = None, applicable_to: str = "", prefix: str = "api/templates") -> None:
        pass  # TODO: implement

    def load_from_file(self, name: str) -> None:
        pass  # TODO: implement

    def render(self, *args: Any, **kwargs: Any) -> str:
        pass  # TODO: implement


ProductTemplate = Template("product", applicable_to="product")
BaseShopTemplate = Template("shop", applicable_to="store")
NotificationTemplate = Template("notification", applicable_to="store")
ForgotPasswordTemplate = Template("forgotpassword", applicable_to="global")
VerifyEmailTemplate = Template("verifyemail", applicable_to="global")
CustomerRefundTemplate = Template("customer_refund", applicable_to="store")
MerchantRefundNotifyTemplate = Template("merchant_refund_notify", applicable_to="store")
SyncinfoTemplate = Template("syncinfo", applicable_to="global")

ALL_TEMPLATES = {template.name: template for template in globals().values() if isinstance(template, Template)}


class TemplateManager:
    pass  # TODO: implement
    def __init__(self) -> None:
        pass  # TODO: implement

    def add_template(self, template: Template) -> None:
        pass  # TODO: implement

    def init_defaults(self) -> None:
        pass  # TODO: implement
