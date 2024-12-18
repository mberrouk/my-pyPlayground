from _typeshed import Incomplete
from django.core.management.color import color_style as color_style
from django.db import IntegrityError as IntegrityError, migrations as migrations, transaction as transaction
from django.db.models import Q as Q

WARNING: str

def update_proxy_model_permissions(apps, schema_editor, reverse: bool = False) -> None: ...
def revert_proxy_model_permissions(apps, schema_editor) -> None: ...

class Migration(migrations.Migration):
    dependencies: Incomplete
    operations: Incomplete
