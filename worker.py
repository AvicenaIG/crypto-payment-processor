import os

if os.getenv("BITCART_OTEL_ENABLED", "false").lower() == "true":


import asyncio
from multiprocessing import Process

from api.logserver import main as start_logserver
from api.logserver import wait_for_port
from api.worker import get_app, start_broker, wait_loop

# TODO: use CLI from taskiq
if __name__ == "__main__":
