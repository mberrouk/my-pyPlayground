from _typeshed import Incomplete
from django import template as template

register: Incomplete

class AdminLogNode(template.Node):
    limit: Incomplete
    varname: Incomplete
    user: Incomplete
    def __init__(self, limit, varname, user) -> None: ...
    def render(self, context): ...

def get_admin_log(parser, token): ...
