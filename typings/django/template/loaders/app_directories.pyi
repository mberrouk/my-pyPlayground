from .filesystem import Loader as FilesystemLoader
from django.template.utils import get_app_template_dirs as get_app_template_dirs

class Loader(FilesystemLoader):
    def get_dirs(self): ...
