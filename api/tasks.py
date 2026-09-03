import json
from decimal import Decimal
from typing import Any

from dishka import FromDishka
from dishka.integrations.taskiq import inject
from taskiq import TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_redis import ListRedisScheduleSource, RedisAsyncResultBackend

from api import utils
from api.ext.moneyformat import currency_table
from api.logging import get_exception_message, get_logger, log_errors
from api.redis import Redis
from api.schemas.tasks import (
)
from api.services.backup_manager import BackupManager
from api.services.coins import CoinService
from api.services.crud.stores import StoreService
from api.services.crud.users import UserService
from api.services.crud.wallets import WalletService
from api.services.exchange_rate import ExchangeRateService
from api.services.ext.configurator import ConfiguratorService
from api.services.host_agent import HostAgentService
from api.services.notification_manager import NotificationManager
from api.services.plugin_registry import PluginRegistry
from api.services.wallet_data import WalletDataService
from api.settings import Settings
from api.types import TasksBroker

logger = get_logger(__name__)

settings = Settings()
broker = TasksBroker(url=settings.redis_url).with_result_backend(
)
client_tasks_broker = TasksBroker(url=settings.redis_url, queue_name="taskiq_client_tasks").with_result_backend(
)
redis_scheduler_source = ListRedisScheduleSource(settings.redis_url)
label_scheduler_resource = LabelScheduleSource(broker)
scheduler = TaskiqScheduler(broker, sources=[label_scheduler_resource, redis_scheduler_source])
del settings


@broker.task("rates_action")
@inject(patch_module=True)
async def rates_action(
) -> str:
    func = getattr(exchange_rate_service, params.func)
        pass  # TODO: implement


@broker.task("agent_call")
@inject(patch_module=True)
async def agent_call(params: AgentCallMessage, host_agent: FromDishka[HostAgentService]) -> dict[str, Any]:


@broker.task("send_verification_email")
@inject(patch_module=True)
async def send_verification_email(params: SendVerificationEmailMessage, user_service: FromDishka[UserService]) -> None:


@broker.task("sync_wallet")
@inject(patch_module=True)
async def sync_wallet(
) -> None:


@broker.task("send_notification")
@inject(patch_module=True)
async def send_notification(
) -> None:


@broker.task("process_new_backup_policy")
@inject(patch_module=True)
async def process_new_backup_policy(params: ProcessNewBackupPolicyMessage, backup_manager: FromDishka[BackupManager]) -> None:


@broker.task("deploy_task")
@inject(patch_module=True)
async def deploy_task(params: DeployTaskMessage, configurator_service: FromDishka[ConfiguratorService]) -> None:


@broker.task("license_changed")
@inject(patch_module=True)
async def license_changed(params: LicenseChangedMessage, plugin_registry: FromDishka[PluginRegistry]) -> None:


# We need two tasks here due to the way taskiq works, with shared task it seems to execute only in one broker
# (the one which is set as default_broker)
@broker.task("plugin_task_server")
@inject(patch_module=True)
async def plugin_task_server(params: PluginTaskMessage, plugin_registry: FromDishka[PluginRegistry]) -> None:


@client_tasks_broker.task("plugin_task_client")
@inject(patch_module=True)
async def plugin_task_client(params: PluginTaskMessage, plugin_registry: FromDishka[PluginRegistry]) -> None:
