from _typeshed import Incomplete
from django.conf import settings as settings
from django.utils.crypto import constant_time_compare as constant_time_compare, salted_hmac as salted_hmac
from django.utils.http import base36_to_int as base36_to_int, int_to_base36 as int_to_base36

class PasswordResetTokenGenerator:
    key_salt: str
    algorithm: Incomplete
    def __init__(self) -> None: ...
    secret: Incomplete
    secret_fallbacks: Incomplete
    def make_token(self, user): ...
    def check_token(self, user, token): ...

default_token_generator: Incomplete
