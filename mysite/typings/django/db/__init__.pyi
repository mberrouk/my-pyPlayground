"""
This type stub file was generated by pyright.
"""

from django.core import signals
from django.db.utils import ConnectionHandler, ConnectionRouter, DEFAULT_DB_ALIAS, DJANGO_VERSION_PICKLE_KEY, DataError, DatabaseError, Error, IntegrityError, InterfaceError, InternalError, NotSupportedError, OperationalError, ProgrammingError
from django.utils.connection import ConnectionProxy

"""
This type stub file was generated by pyright.
"""
__all__ = ["close_old_connections", "connection", "connections", "reset_queries", "router", "DatabaseError", "IntegrityError", "InternalError", "ProgrammingError", "DataError", "NotSupportedError", "Error", "InterfaceError", "OperationalError", "DEFAULT_DB_ALIAS", "DJANGO_VERSION_PICKLE_KEY"]
connections = ...
router = ...
connection = ...
def reset_queries(**kwargs):
    ...

def close_old_connections(**kwargs):
    ...

