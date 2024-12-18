from _typeshed import Incomplete
from django.urls import reverse as reverse
from django.utils.safestring import mark_safe as mark_safe

docutils_is_available: bool

def get_view_name(view_func): ...
def parse_docstring(docstring): ...
def parse_rst(text, default_reference_context, thing_being_parsed: Incomplete | None = None): ...

ROLES: Incomplete

def create_reference_role(rolename, urlbase): ...
def default_reference_role(name, rawtext, text, lineno, inliner, options: Incomplete | None = None, content: Incomplete | None = None): ...

named_group_matcher: Incomplete
unnamed_group_matcher: Incomplete
non_capturing_group_matcher: Incomplete

def replace_metacharacters(pattern): ...
def replace_named_groups(pattern): ...
def replace_unnamed_groups(pattern): ...
def remove_non_capturing_groups(pattern): ...
