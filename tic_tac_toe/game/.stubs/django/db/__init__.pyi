"""
This type stub file was generated by pyright.
"""

from typing import Any
from .backends.base.base import BaseDatabaseWrapper
from .utils import ConnectionHandler, ConnectionRouter, DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, DJANGO_VERSION_PICKLE_KEY as DJANGO_VERSION_PICKLE_KEY, DataError as DataError, DatabaseError as DatabaseError, Error as Error, IntegrityError as IntegrityError, InterfaceError as InterfaceError, InternalError as InternalError, NotSupportedError as NotSupportedError, OperationalError as OperationalError, ProgrammingError as ProgrammingError

connections: ConnectionHandler
router: ConnectionRouter
connection: BaseDatabaseWrapper
def close_old_connections(**kwargs: Any) -> None:
    ...

def reset_queries(**kwargs: Any) -> None:
    ...

