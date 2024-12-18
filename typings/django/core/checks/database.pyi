from . import Tags as Tags, register as register
from _typeshed import Incomplete
from django.db import connections as connections

def check_database_backends(databases: Incomplete | None = None, **kwargs): ...
