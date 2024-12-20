from _typeshed import Incomplete
from collections.abc import Generator

class ContextPopException(Exception): ...

class ContextDict(dict):
    context: Incomplete
    def __init__(self, context, *args, **kwargs) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args, **kwargs) -> None: ...

class BaseContext:
    def __init__(self, dict_: Incomplete | None = None) -> None: ...
    def __copy__(self): ...
    def __iter__(self): ...
    def push(self, *args, **kwargs): ...
    def pop(self): ...
    def __setitem__(self, key, value) -> None: ...
    def set_upward(self, key, value) -> None: ...
    def __getitem__(self, key): ...
    def __delitem__(self, key) -> None: ...
    def __contains__(self, key) -> bool: ...
    def get(self, key, otherwise: Incomplete | None = None): ...
    def setdefault(self, key, default: Incomplete | None = None): ...
    def new(self, values: Incomplete | None = None): ...
    def flatten(self): ...
    def __eq__(self, other): ...

class Context(BaseContext):
    autoescape: Incomplete
    use_l10n: Incomplete
    use_tz: Incomplete
    template_name: str
    render_context: Incomplete
    template: Incomplete
    def __init__(self, dict_: Incomplete | None = None, autoescape: bool = True, use_l10n: Incomplete | None = None, use_tz: Incomplete | None = None) -> None: ...
    def bind_template(self, template) -> Generator[None]: ...
    def __copy__(self): ...
    def update(self, other_dict): ...

class RenderContext(BaseContext):
    template: Incomplete
    def __iter__(self): ...
    def __contains__(self, key) -> bool: ...
    def get(self, key, otherwise: Incomplete | None = None): ...
    def __getitem__(self, key): ...
    def push_state(self, template, isolated_context: bool = True) -> Generator[None]: ...

class RequestContext(Context):
    request: Incomplete
    def __init__(self, request, dict_: Incomplete | None = None, processors: Incomplete | None = None, use_l10n: Incomplete | None = None, use_tz: Incomplete | None = None, autoescape: bool = True) -> None: ...
    template: Incomplete
    def bind_template(self, template) -> Generator[None]: ...
    def new(self, values: Incomplete | None = None): ...

def make_context(context, request: Incomplete | None = None, **kwargs): ...
