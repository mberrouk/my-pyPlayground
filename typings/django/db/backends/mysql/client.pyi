from django.db.backends.base.client import BaseDatabaseClient as BaseDatabaseClient

class DatabaseClient(BaseDatabaseClient):
    executable_name: str
    @classmethod
    def settings_to_cmd_args_env(cls, settings_dict, parameters): ...
    def runshell(self, parameters) -> None: ...
