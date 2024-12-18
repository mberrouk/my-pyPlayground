from django.core.mail.backends.base import BaseEmailBackend as BaseEmailBackend

class EmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages): ...
