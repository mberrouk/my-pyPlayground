from _typeshed import Incomplete
from django.utils.inspect import func_accepts_kwargs as func_accepts_kwargs

class Tags:
    admin: str
    async_support: str
    caches: str
    compatibility: str
    database: str
    files: str
    models: str
    security: str
    signals: str
    sites: str
    staticfiles: str
    templates: str
    translation: str
    urls: str

class CheckRegistry:
    registered_checks: Incomplete
    deployment_checks: Incomplete
    def __init__(self) -> None: ...
    def register(self, check: Incomplete | None = None, *tags, **kwargs): ...
    def run_checks(self, app_configs: Incomplete | None = None, tags: Incomplete | None = None, include_deployment_checks: bool = False, databases: Incomplete | None = None): ...
    def tag_exists(self, tag, include_deployment_checks: bool = False): ...
    def tags_available(self, deployment_checks: bool = False): ...
    def get_checks(self, include_deployment_checks: bool = False): ...

registry: Incomplete
register: Incomplete
run_checks: Incomplete
tag_exists: Incomplete
