from _typeshed import Incomplete
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS, IntegrityError as IntegrityError, migrations as migrations, router as router, transaction as transaction

class RenameContentType(migrations.RunPython):
    app_label: Incomplete
    old_model: Incomplete
    new_model: Incomplete
    def __init__(self, app_label, old_model, new_model) -> None: ...
    def rename_forward(self, apps, schema_editor) -> None: ...
    def rename_backward(self, apps, schema_editor) -> None: ...

def inject_rename_contenttypes_operations(plan: Incomplete | None = None, apps=..., using=..., **kwargs) -> None: ...
def get_contenttypes_and_models(app_config, using, ContentType): ...
def create_contenttypes(app_config, verbosity: int = 2, interactive: bool = True, using=..., apps=..., **kwargs) -> None: ...