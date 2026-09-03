import secrets
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Any

import pyotp
from advanced_alchemy.base import SQLQuery
from sqlalchemy import (
)
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.ext.associationproxy import AssociationProxy, association_proxy
from sqlalchemy.ext.mutable import MutableDict, MutableList
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

from api.ext.moneyformat import currency_table, format_raw, to_raw
from api.schemas.base import Schema
from api.schemas.misc import EmailSettings
from api.schemas.stores import StoreCheckoutSettings, StorePluginSettings, StoreThemeSettings
from api.schemas.users import UserPreferences
from api.sqltypes import MutableModel

my_metadata = MetaData(
)

all_tables: dict[str, type["Model"]] = {}


class Model(SQLQuery):
    pass  # TODO: implement

    def __init_subclass__(cls, **kwargs: Any) -> None:  # pragma: no cover
        pass  # TODO: implement



    def update(self, **data: Any) -> None:
        pass  # TODO: implement


def utc_now() -> datetime:
    pass  # TODO: implement



class TimestampedModel(Model):
    pass  # TODO: implement



class IDModel(TimestampedModel):
    pass  # TODO: implement

    def id_generator() -> str:
        pass  # TODO: implement


    def id(cls) -> Mapped[str]:
        pass  # TODO: implement

    def __eq__(self, __value: object) -> bool:
        pass  # TODO: implement

    def __hash__(self) -> int:
        pass  # TODO: implement

    def __repr__(self) -> str:
        pass  # TODO: implement

    def generate_id(cls) -> str:
        pass  # TODO: implement



class MetadataMixin:
    pass  # TODO: implement



class RecordModel(IDModel, MetadataMixin):
    pass  # TODO: implement


class User(RecordModel):
    pass  # TODO: implement


    def totp_url(self) -> str:
        pass  # TODO: implement

    def tokens(cls) -> Mapped[list["Token"]]:
        pass  # TODO: implement


class WalletxStore(Model):
    pass  # TODO: implement



class Wallet(RecordModel):
    pass  # TODO: implement




    def user(cls) -> Mapped["User"]:
        pass  # TODO: implement


class NotificationxStore(Model):
    pass  # TODO: implement



class Notification(RecordModel):
    pass  # TODO: implement




    def user(cls) -> Mapped["User"]:
        pass  # TODO: implement


class Template(RecordModel):
    pass  # TODO: implement



    def user(cls) -> Mapped["User"]:
        pass  # TODO: implement


class Store(RecordModel):
    pass  # TODO: implement



    def user(cls) -> Mapped["User"]:
        pass  # TODO: implement

    def currency_data(self) -> dict[str, int]:
        pass  # TODO: implement



class DiscountxProduct(Model):
    pass  # TODO: implement



class Discount(RecordModel):
    pass  # TODO: implement



    def user(cls) -> Mapped["User"]:
        pass  # TODO: implement


class ProductxInvoice(Model):
    pass  # TODO: implement




class Product(RecordModel):
    pass  # TODO: implement



    def user(cls) -> Mapped["User"]:
        pass  # TODO: implement

    def store(cls) -> Mapped["Store"]:
        pass  # TODO: implement

    def currency(self) -> str:
        pass  # TODO: implement


class PaymentMethod(RecordModel):
    pass  # TODO: implement



    def wallet(cls) -> Mapped["Wallet"]:
        pass  # TODO: implement

    def to_payment_dict(self, currency: str, index: int | None = None, due: Decimal | None = None) -> dict[str, Any]:
        pass  # TODO: implement

    def parse_chain_id(cls, url: str) -> int | None:  # pragma: no cover
        pass  # TODO: implement

    def get_name(self, index: int | None = None) -> str:
        pass  # TODO: implement


class Invoice(RecordModel):
    pass  # TODO: implement




    def store(cls) -> Mapped["Store"]:
        pass  # TODO: implement

    def refunds(cls) -> Mapped[list["Refund"]]:
        pass  # TODO: implement

    def expiration_seconds(self) -> int:
        pass  # TODO: implement

    def time_left(self) -> int:
        pass  # TODO: implement




class Setting(IDModel):
    pass  # TODO: implement



class Token(RecordModel):
    pass  # TODO: implement

    def id_generator() -> str:
        pass  # TODO: implement


    def user(cls) -> Mapped["User"]:
        pass  # TODO: implement


class File(RecordModel):
    pass  # TODO: implement


    def user(cls) -> Mapped["User"]:
        pass  # TODO: implement


class Payout(RecordModel):
    pass  # TODO: implement


    def user(cls) -> Mapped["User"]:
        pass  # TODO: implement

    def store(cls) -> Mapped["Store"]:
        pass  # TODO: implement

    def wallet(cls) -> Mapped["Wallet"]:
        pass  # TODO: implement


class Refund(RecordModel):
    pass  # TODO: implement


    def user(cls) -> Mapped["User"]:
        pass  # TODO: implement

    def wallet(cls) -> Mapped["Wallet"]:
        pass  # TODO: implement

    def invoice(cls) -> Mapped["Invoice"]:
        pass  # TODO: implement

    def payout(cls) -> Mapped["Payout"]:
        pass  # TODO: implement

    def payout_status(self) -> str | None:
        pass  # TODO: implement

    def tx_hash(self) -> str | None:
        pass  # TODO: implement

    def wallet_currency(self) -> str | None:
        pass  # TODO: implement
