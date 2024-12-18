from _typeshed import Incomplete
from django.db.utils import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, DJANGO_VERSION_PICKLE_KEY as DJANGO_VERSION_PICKLE_KEY, DataError as DataError, DatabaseError as DatabaseError, Error as Error, IntegrityError as IntegrityError, InterfaceError as InterfaceError, InternalError as InternalError, NotSupportedError as NotSupportedError, OperationalError as OperationalError, ProgrammingError as ProgrammingError

__all__ = ['close_old_connections', 'connection', 'connections', 'reset_queries', 'router', 'DatabaseError', 'IntegrityError', 'InternalError', 'ProgrammingError', 'DataError', 'NotSupportedError', 'Error', 'InterfaceError', 'OperationalError', 'DEFAULT_DB_ALIAS', 'DJANGO_VERSION_PICKLE_KEY']

connections: Incomplete
router: Incomplete
connection: Incomplete

def reset_queries(**kwargs) -> None: ...
def close_old_connections(**kwargs) -> None: ...
