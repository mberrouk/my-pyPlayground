from django.core.management.commands.inspectdb import Command as InspectDBCommand

class Command(InspectDBCommand):
    db_module: str
    def get_field_type(self, connection, table_name, row): ...
