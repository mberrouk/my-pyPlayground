from django.core.exceptions import ViewDoesNotExist as ViewDoesNotExist
from django.utils.module_loading import module_has_submodule as module_has_submodule

def get_callable(lookup_view): ...
def get_mod_func(callback): ...
