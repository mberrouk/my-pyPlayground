from django.db.backends.base.client import BaseDatabaseClient as BaseDatabaseClient

class DatabaseClient(BaseDatabaseClient):
    executable_name: str
    wrapper_name: str
    @staticmethod
    def connect_string(settings_dict): ...
    @classmethod
    def settings_to_cmd_args_env(cls, settings_dict, parameters): ...
