from _typeshed import Incomplete
from django.apps import AppConfig as AppConfig
from django.contrib.messages.storage import base as base
from django.contrib.messages.utils import get_level_tags as get_level_tags
from django.core.signals import setting_changed as setting_changed
from django.utils.functional import SimpleLazyObject as SimpleLazyObject

def update_level_tags(setting, **kwargs) -> None: ...

class MessagesConfig(AppConfig):
    name: str
    verbose_name: Incomplete
    def ready(self) -> None: ...
