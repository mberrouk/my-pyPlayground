from _typeshed import Incomplete
from django.conf import settings as settings
from django.core import paginator as paginator
from django.core.exceptions import ImproperlyConfigured as ImproperlyConfigured
from django.utils import translation as translation

class Sitemap:
    limit: int
    protocol: Incomplete
    i18n: bool
    languages: Incomplete
    alternates: bool
    x_default: bool
    def get_languages_for_item(self, item): ...
    @property
    def paginator(self): ...
    def items(self): ...
    def location(self, item): ...
    def get_protocol(self, protocol: Incomplete | None = None): ...
    def get_domain(self, site: Incomplete | None = None): ...
    def get_urls(self, page: int = 1, site: Incomplete | None = None, protocol: Incomplete | None = None): ...
    def get_latest_lastmod(self): ...

class GenericSitemap(Sitemap):
    priority: Incomplete
    changefreq: Incomplete
    queryset: Incomplete
    date_field: Incomplete
    protocol: Incomplete
    def __init__(self, info_dict, priority: Incomplete | None = None, changefreq: Incomplete | None = None, protocol: Incomplete | None = None) -> None: ...
    def items(self): ...
    def lastmod(self, item): ...
    def get_latest_lastmod(self): ...