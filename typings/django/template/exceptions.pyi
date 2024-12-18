from _typeshed import Incomplete

class TemplateDoesNotExist(Exception):
    backend: Incomplete
    tried: Incomplete
    chain: Incomplete
    def __init__(self, msg, tried: Incomplete | None = None, backend: Incomplete | None = None, chain: Incomplete | None = None) -> None: ...

class TemplateSyntaxError(Exception): ...
