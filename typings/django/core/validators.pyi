from _typeshed import Incomplete
from django.core.exceptions import ValidationError as ValidationError
from django.utils.deconstruct import deconstructible as deconstructible
from django.utils.encoding import punycode as punycode
from django.utils.ipv6 import is_valid_ipv6_address as is_valid_ipv6_address
from django.utils.translation import ngettext_lazy as ngettext_lazy

EMPTY_VALUES: Incomplete

class RegexValidator:
    regex: str
    message: Incomplete
    code: str
    inverse_match: bool
    flags: int
    def __init__(self, regex: Incomplete | None = None, message: Incomplete | None = None, code: Incomplete | None = None, inverse_match: Incomplete | None = None, flags: Incomplete | None = None) -> None: ...
    def __call__(self, value) -> None: ...
    def __eq__(self, other): ...

class DomainNameValidator(RegexValidator):
    message: Incomplete
    ul: str
    hostname_re: Incomplete
    domain_re: Incomplete
    tld_re: Incomplete
    ascii_only_hostname_re: str
    ascii_only_domain_re: str
    ascii_only_tld_re: str
    max_length: int
    accept_idna: Incomplete
    regex: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def __call__(self, value) -> None: ...

validate_domain_name: Incomplete

class URLValidator(RegexValidator):
    ul: str
    ipv4_re: str
    ipv6_re: str
    hostname_re: Incomplete
    domain_re: Incomplete
    tld_re: Incomplete
    host_re: Incomplete
    regex: Incomplete
    message: Incomplete
    schemes: Incomplete
    unsafe_chars: Incomplete
    max_length: int
    def __init__(self, schemes: Incomplete | None = None, **kwargs) -> None: ...
    def __call__(self, value) -> None: ...

integer_validator: Incomplete

def validate_integer(value): ...

class EmailValidator:
    message: Incomplete
    code: str
    user_regex: Incomplete
    domain_regex: Incomplete
    literal_regex: Incomplete
    domain_allowlist: Incomplete
    def __init__(self, message: Incomplete | None = None, code: Incomplete | None = None, allowlist: Incomplete | None = None) -> None: ...
    def __call__(self, value) -> None: ...
    def validate_domain_part(self, domain_part): ...
    def __eq__(self, other): ...

validate_email: Incomplete
slug_re: Incomplete
validate_slug: Incomplete
slug_unicode_re: Incomplete
validate_unicode_slug: Incomplete

def validate_ipv4_address(value) -> None: ...
def validate_ipv6_address(value) -> None: ...
def validate_ipv46_address(value) -> None: ...

ip_address_validator_map: Incomplete

def ip_address_validators(protocol, unpack_ipv4): ...
def int_list_validator(sep: str = ',', message: Incomplete | None = None, code: str = 'invalid', allow_negative: bool = False): ...

validate_comma_separated_integer_list: Incomplete

class BaseValidator:
    message: Incomplete
    code: str
    limit_value: Incomplete
    def __init__(self, limit_value, message: Incomplete | None = None) -> None: ...
    def __call__(self, value) -> None: ...
    def __eq__(self, other): ...
    def compare(self, a, b): ...
    def clean(self, x): ...

class MaxValueValidator(BaseValidator):
    message: Incomplete
    code: str
    def compare(self, a, b): ...

class MinValueValidator(BaseValidator):
    message: Incomplete
    code: str
    def compare(self, a, b): ...

class StepValueValidator(BaseValidator):
    message: Incomplete
    code: str
    offset: Incomplete
    def __init__(self, limit_value, message: Incomplete | None = None, offset: Incomplete | None = None) -> None: ...
    def __call__(self, value) -> None: ...
    def compare(self, a, b): ...

class MinLengthValidator(BaseValidator):
    message: Incomplete
    code: str
    def compare(self, a, b): ...
    def clean(self, x): ...

class MaxLengthValidator(BaseValidator):
    message: Incomplete
    code: str
    def compare(self, a, b): ...
    def clean(self, x): ...

class DecimalValidator:
    messages: Incomplete
    max_digits: Incomplete
    decimal_places: Incomplete
    def __init__(self, max_digits, decimal_places) -> None: ...
    def __call__(self, value) -> None: ...
    def __eq__(self, other): ...

class FileExtensionValidator:
    message: Incomplete
    code: str
    allowed_extensions: Incomplete
    def __init__(self, allowed_extensions: Incomplete | None = None, message: Incomplete | None = None, code: Incomplete | None = None) -> None: ...
    def __call__(self, value) -> None: ...
    def __eq__(self, other): ...

def get_available_image_extensions(): ...
def validate_image_file_extension(value): ...

class ProhibitNullCharactersValidator:
    message: Incomplete
    code: str
    def __init__(self, message: Incomplete | None = None, code: Incomplete | None = None) -> None: ...
    def __call__(self, value) -> None: ...
    def __eq__(self, other): ...
