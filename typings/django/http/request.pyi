from _typeshed import Incomplete
from django.conf import settings as settings
from django.core import signing as signing
from django.core.exceptions import BadRequest as BadRequest, DisallowedHost as DisallowedHost, ImproperlyConfigured as ImproperlyConfigured, RequestDataTooBig as RequestDataTooBig, TooManyFieldsSent as TooManyFieldsSent
from django.core.files import uploadhandler as uploadhandler
from django.http.multipartparser import MultiPartParser as MultiPartParser, MultiPartParserError as MultiPartParserError, TooManyFilesSent as TooManyFilesSent
from django.utils.datastructures import CaseInsensitiveMapping as CaseInsensitiveMapping, ImmutableList as ImmutableList, MultiValueDict as MultiValueDict
from django.utils.encoding import escape_uri_path as escape_uri_path, iri_to_uri as iri_to_uri
from django.utils.functional import cached_property as cached_property
from django.utils.http import is_same_domain as is_same_domain, parse_header_parameters as parse_header_parameters

RAISE_ERROR: Incomplete
host_validation_re: Incomplete

class UnreadablePostError(OSError): ...
class RawPostDataException(Exception): ...

class HttpRequest:
    GET: Incomplete
    POST: Incomplete
    COOKIES: Incomplete
    META: Incomplete
    FILES: Incomplete
    path: str
    path_info: str
    method: Incomplete
    resolver_match: Incomplete
    content_type: Incomplete
    content_params: Incomplete
    def __init__(self) -> None: ...
    def headers(self): ...
    def accepted_types(self): ...
    def accepts(self, media_type): ...
    def get_host(self): ...
    def get_port(self): ...
    def get_full_path(self, force_append_slash: bool = False): ...
    def get_full_path_info(self, force_append_slash: bool = False): ...
    def get_signed_cookie(self, key, default=..., salt: str = '', max_age: Incomplete | None = None): ...
    def build_absolute_uri(self, location: Incomplete | None = None): ...
    @property
    def scheme(self): ...
    def is_secure(self): ...
    @property
    def encoding(self): ...
    @encoding.setter
    def encoding(self, val) -> None: ...
    @property
    def upload_handlers(self): ...
    @upload_handlers.setter
    def upload_handlers(self, upload_handlers) -> None: ...
    def parse_file_upload(self, META, post_data): ...
    @property
    def body(self): ...
    def close(self) -> None: ...
    def read(self, *args, **kwargs): ...
    def readline(self, *args, **kwargs): ...
    def __iter__(self): ...
    def readlines(self): ...

class HttpHeaders(CaseInsensitiveMapping):
    HTTP_PREFIX: str
    UNPREFIXED_HEADERS: Incomplete
    def __init__(self, environ) -> None: ...
    def __getitem__(self, key): ...
    @classmethod
    def parse_header_name(cls, header): ...
    @classmethod
    def to_wsgi_name(cls, header): ...
    @classmethod
    def to_asgi_name(cls, header): ...
    @classmethod
    def to_wsgi_names(cls, headers): ...
    @classmethod
    def to_asgi_names(cls, headers): ...

class QueryDict(MultiValueDict):
    def __init__(self, query_string: Incomplete | None = None, mutable: bool = False, encoding: Incomplete | None = None) -> None: ...
    @classmethod
    def fromkeys(cls, iterable, value: str = '', mutable: bool = False, encoding: Incomplete | None = None): ...
    @property
    def encoding(self): ...
    @encoding.setter
    def encoding(self, value) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def setlist(self, key, list_) -> None: ...
    def setlistdefault(self, key, default_list: Incomplete | None = None): ...
    def appendlist(self, key, value) -> None: ...
    def pop(self, key, *args): ...
    def popitem(self): ...
    def clear(self) -> None: ...
    def setdefault(self, key, default: Incomplete | None = None): ...
    def copy(self): ...
    def urlencode(self, safe: Incomplete | None = None): ...

class MediaType:
    def __init__(self, media_type_raw_line) -> None: ...
    @property
    def is_all_types(self): ...
    def match(self, other): ...

def bytes_to_text(s, encoding): ...
def split_domain_port(host): ...
def validate_host(host, allowed_hosts): ...
def parse_accept_header(header): ...
