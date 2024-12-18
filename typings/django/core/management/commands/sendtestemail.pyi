from django.core.mail import mail_admins as mail_admins, mail_managers as mail_managers, send_mail as send_mail
from django.core.management.base import BaseCommand as BaseCommand
from django.utils import timezone as timezone

class Command(BaseCommand):
    help: str
    missing_args_message: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **kwargs) -> None: ...
