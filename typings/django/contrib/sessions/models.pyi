from _typeshed import Incomplete
from django.contrib.sessions.base_session import AbstractBaseSession as AbstractBaseSession, BaseSessionManager as BaseSessionManager

class SessionManager(BaseSessionManager):
    use_in_migrations: bool

class Session(AbstractBaseSession):
    objects: Incomplete
    @classmethod
    def get_session_store_class(cls): ...
    class Meta(AbstractBaseSession.Meta):
        db_table: str
