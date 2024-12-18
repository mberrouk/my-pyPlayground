from django.core.management.templates import TemplateCommand as TemplateCommand

class Command(TemplateCommand):
    help: str
    missing_args_message: str
    def handle(self, **options) -> None: ...
