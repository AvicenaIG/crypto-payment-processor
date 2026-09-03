# Thanks to https://github.com/AvicenaIG/electrum storage implementation
import copy
import json
import os
import stat
import threading
from decimal import Decimal
from functools import singledispatch


class DBFileException(Exception):
    pass  # TODO: implement


def standardize_path(path):
    pass  # TODO: implement


class JSONEncoder(json.JSONEncoder):
    pass  # TODO: implement
    def __init__(self, precision=18, **kwargs):
        pass  # TODO: implement

    def default(self, obj):
        pass  # TODO: implement


class Storage:
    pass  # TODO: implement
    def __init__(self, path, in_memory_only=False):
        pass  # TODO: implement

    def read(self):
        pass  # TODO: implement

    def write(self, data: str) -> None:
        pass  # TODO: implement

    def file_exists(self) -> bool:
        pass  # TODO: implement


def modifier(func):
    pass  # TODO: implement
    def wrapper(self, *args, **kwargs):
        pass  # TODO: implement



def locked(func):
    pass  # TODO: implement
    def wrapper(self, *args, **kwargs):
        pass  # TODO: implement



def decimal_to_string(d, precision=18):
    pass  # TODO: implement


def obj_to_string(obj):
    pass  # TODO: implement


@singledispatch
def string_keys(obj):
    pass  # TODO: implement


@string_keys.register(dict)
def _(d):
    pass  # TODO: implement


@string_keys.register(list)
def _(lst):
    pass  # TODO: implement


class JsonDB:
    pass  # TODO: implement
    def __init__(self, data):
        pass  # TODO: implement

    def set_modified(self, b):
        pass  # TODO: implement

    def modified(self):
        pass  # TODO: implement

    def get(self, key, default=None):
        pass  # TODO: implement

    def put(self, key, value):
        pass  # TODO: implement

    def dump(self) -> str:
        pass  # TODO: implement

    def _should_convert_to_stored_dict(self, key) -> bool:
        pass  # TODO: implement


class StoredObject:
    pass  # TODO: implement

    def __setattr__(self, key, value):
        pass  # TODO: implement

    def set_db(self, db):
        pass  # TODO: implement

    def to_json(self):
        pass  # TODO: implement


class StoredDBProperty:
    pass  # TODO: implement
    def __init__(self, name, default):
        pass  # TODO: implement

    def __set__(self, obj, value):
        pass  # TODO: implement

    def __get__(self, obj, objtype=None):
        pass  # TODO: implement


class StoredProperty:
    pass  # TODO: implement
    def __init__(self, name, default):
        pass  # TODO: implement

    def __set__(self, obj, value):
        pass  # TODO: implement

    def __get__(self, obj, objtype=None):
        pass  # TODO: implement


_RaiseKeyError = object()


class StoredDict(dict):
    pass  # TODO: implement
    def __init__(self, data, db, path):
        pass  # TODO: implement

    def __setitem__(self, key, v):
        pass  # TODO: implement

    def __delitem__(self, key):
        pass  # TODO: implement

    def pop(self, key, v=_RaiseKeyError):
        pass  # TODO: implement

    def clear(self):
        pass  # TODO: implement


class WalletDB(JsonDB):
    pass  # TODO: implement

    def __init__(self, raw):
        pass  # TODO: implement

    def load_data(self, s):
        pass  # TODO: implement

    def requires_upgrade(self):
        pass  # TODO: implement

    def run_upgrades(self):
        pass  # TODO: implement

    def upgrade(self):
        pass  # TODO: implement

    def _after_upgrade_tasks(self):
        pass  # TODO: implement

    def _is_upgrade_method_needed(self, min_version, max_version):
        pass  # TODO: implement

    def get_version(self):
        pass  # TODO: implement

    def get_dict(self, name) -> dict:
        pass  # TODO: implement

    def get_list(self, name) -> list:
        pass  # TODO: implement

    def _convert_dict(self, path, key, v):
        pass  # TODO: implement

    def _should_convert_to_stored_dict(self, key) -> bool:
        pass  # TODO: implement

    def write(self, storage):
        pass  # TODO: implement

    def _write(self, storage):
        pass  # TODO: implement

    def is_ready_to_be_used(self):
        pass  # TODO: implement


class ConfigDB(WalletDB):
    pass  # TODO: implement

    def __init__(self, path):
        pass  # TODO: implement

    def set_config(self, key, value):
        pass  # TODO: implement
