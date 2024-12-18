from _typeshed import Incomplete
from django.conf import settings as settings
from django.contrib.admin.utils import quote as quote
from django.contrib.contenttypes.models import ContentType as ContentType
from django.db import models as models
from django.urls import NoReverseMatch as NoReverseMatch, reverse as reverse
from django.utils import timezone as timezone
from django.utils.deprecation import RemovedInDjango60Warning as RemovedInDjango60Warning
from django.utils.text import get_text_list as get_text_list
from django.utils.translation import gettext as gettext

ADDITION: int
CHANGE: int
DELETION: int
ACTION_FLAG_CHOICES: Incomplete

class LogEntryManager(models.Manager):
    use_in_migrations: bool
    def log_action(self, user_id, content_type_id, object_id, object_repr, action_flag, change_message: str = ''): ...
    def log_actions(self, user_id, queryset, action_flag, change_message: str = '', *, single_object: bool = False): ...

class LogEntry(models.Model):
    action_time: Incomplete
    user: Incomplete
    content_type: Incomplete
    object_id: Incomplete
    object_repr: Incomplete
    action_flag: Incomplete
    change_message: Incomplete
    objects: Incomplete
    class Meta:
        verbose_name: Incomplete
        verbose_name_plural: Incomplete
        db_table: str
        ordering: Incomplete
    def is_addition(self): ...
    def is_change(self): ...
    def is_deletion(self): ...
    def get_change_message(self): ...
    def get_edited_object(self): ...
    def get_admin_url(self): ...
