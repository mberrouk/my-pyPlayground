from _typeshed import Incomplete
from django.core.cache import InvalidCacheBackendError as InvalidCacheBackendError, caches as caches
from django.core.cache.utils import make_template_fragment_key as make_template_fragment_key
from django.template import Library as Library, Node as Node, TemplateSyntaxError as TemplateSyntaxError, VariableDoesNotExist as VariableDoesNotExist

register: Incomplete

class CacheNode(Node):
    nodelist: Incomplete
    expire_time_var: Incomplete
    fragment_name: Incomplete
    vary_on: Incomplete
    cache_name: Incomplete
    def __init__(self, nodelist, expire_time_var, fragment_name, vary_on, cache_name) -> None: ...
    def render(self, context): ...

def do_cache(parser, token): ...
