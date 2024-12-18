from _typeshed import Incomplete
from django.conf import settings as settings
from django.core.exceptions import FieldDoesNotExist as FieldDoesNotExist, ImproperlyConfigured as ImproperlyConfigured, ValidationError as ValidationError
from django.utils.functional import cached_property as cached_property, lazy as lazy
from django.utils.html import format_html as format_html, format_html_join as format_html_join
from django.utils.module_loading import import_string as import_string
from django.utils.translation import ngettext as ngettext

def get_default_password_validators(): ...
def get_password_validators(validator_config): ...
def validate_password(password, user: Incomplete | None = None, password_validators: Incomplete | None = None) -> None: ...
def password_changed(password, user: Incomplete | None = None, password_validators: Incomplete | None = None) -> None: ...
def password_validators_help_texts(password_validators: Incomplete | None = None): ...

password_validators_help_text_html: Incomplete

class MinimumLengthValidator:
    min_length: Incomplete
    def __init__(self, min_length: int = 8) -> None: ...
    def validate(self, password, user: Incomplete | None = None) -> None: ...
    def get_help_text(self): ...

def exceeds_maximum_length_ratio(password, max_similarity, value): ...

class UserAttributeSimilarityValidator:
    DEFAULT_USER_ATTRIBUTES: Incomplete
    user_attributes: Incomplete
    max_similarity: Incomplete
    def __init__(self, user_attributes=..., max_similarity: float = 0.7) -> None: ...
    def validate(self, password, user: Incomplete | None = None) -> None: ...
    def get_help_text(self): ...

class CommonPasswordValidator:
    def DEFAULT_PASSWORD_LIST_PATH(self): ...
    passwords: Incomplete
    def __init__(self, password_list_path=...) -> None: ...
    def validate(self, password, user: Incomplete | None = None) -> None: ...
    def get_help_text(self): ...

class NumericPasswordValidator:
    def validate(self, password, user: Incomplete | None = None) -> None: ...
    def get_help_text(self): ...