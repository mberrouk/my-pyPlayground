from django.apps import apps as apps
from django.utils.autoreload import is_django_module as is_django_module

def watch_for_translation_changes(sender, **kwargs) -> None: ...
def translation_file_changed(sender, file_path, **kwargs): ...
