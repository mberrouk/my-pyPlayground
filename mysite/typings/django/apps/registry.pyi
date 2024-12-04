"""
This type stub file was generated by pyright.
"""

import functools

"""
This type stub file was generated by pyright.
"""
class Apps:
    """
    A registry that stores the configuration of installed applications.

    It also keeps track of models, e.g. to provide reverse relations.
    """
    def __init__(self, installed_apps=...) -> None:
        ...
    
    def populate(self, installed_apps=...):
        """
        Load application configurations and models.

        Import each application module and then each model module.

        It is thread-safe and idempotent, but not reentrant.
        """
        ...
    
    def check_apps_ready(self):
        """Raise an exception if all apps haven't been imported yet."""
        ...
    
    def check_models_ready(self):
        """Raise an exception if all models haven't been imported yet."""
        ...
    
    def get_app_configs(self):
        """Import applications and return an iterable of app configs."""
        ...
    
    def get_app_config(self, app_label):
        """
        Import applications and returns an app config for the given label.

        Raise LookupError if no application exists with this label.
        """
        ...
    
    @functools.cache
    def get_models(self, include_auto_created=..., include_swapped=...):
        """
        Return a list of all installed models.

        By default, the following models aren't included:

        - auto-created models for many-to-many relations without
          an explicit intermediate table,
        - models that have been swapped out.

        Set the corresponding keyword argument to True to include such models.
        """
        ...
    
    def get_model(self, app_label, model_name=..., require_ready=...):
        """
        Return the model matching the given app_label and model_name.

        As a shortcut, app_label may be in the form <app_label>.<model_name>.

        model_name is case-insensitive.

        Raise LookupError if no application exists with this label, or no
        model exists with this name in the application. Raise ValueError if
        called with a single argument that doesn't contain exactly one dot.
        """
        ...
    
    def register_model(self, app_label, model):
        ...
    
    def is_installed(self, app_name):
        """
        Check whether an application with this name exists in the registry.

        app_name is the full name of the app e.g. 'django.contrib.admin'.
        """
        ...
    
    def get_containing_app_config(self, object_name):
        """
        Look for an app config containing a given object.

        object_name is the dotted Python path to the object.

        Return the app config for the inner application in case of nesting.
        Return None if the object isn't in any registered app config.
        """
        ...
    
    def get_registered_model(self, app_label, model_name):
        """
        Similar to get_model(), but doesn't require that an app exists with
        the given app_label.

        It's safe to call this method at import time, even while the registry
        is being populated.
        """
        ...
    
    @functools.cache
    def get_swappable_settings_name(self, to_string):
        """
        For a given model string (e.g. "auth.User"), return the name of the
        corresponding settings name if it refers to a swappable model. If the
        referred model is not swappable, return None.

        This method is decorated with @functools.cache because it's performance
        critical when it comes to migrations. Since the swappable settings don't
        change after Django has loaded the settings, there is no reason to get
        the respective settings attribute over and over again.
        """
        ...
    
    def set_available_apps(self, available):
        """
        Restrict the set of installed apps used by get_app_config[s].

        available must be an iterable of application names.

        set_available_apps() must be balanced with unset_available_apps().

        Primarily used for performance optimization in TransactionTestCase.

        This method is safe in the sense that it doesn't trigger any imports.
        """
        ...
    
    def unset_available_apps(self):
        """Cancel a previous call to set_available_apps()."""
        ...
    
    def set_installed_apps(self, installed):
        """
        Enable a different set of installed apps for get_app_config[s].

        installed must be an iterable in the same format as INSTALLED_APPS.

        set_installed_apps() must be balanced with unset_installed_apps(),
        even if it exits with an exception.

        Primarily used as a receiver of the setting_changed signal in tests.

        This method may trigger new imports, which may add new models to the
        registry of all imported models. They will stay in the registry even
        after unset_installed_apps(). Since it isn't possible to replay
        imports safely (e.g. that could lead to registering listeners twice),
        models are registered when they're imported and never removed.
        """
        ...
    
    def unset_installed_apps(self):
        """Cancel a previous call to set_installed_apps()."""
        ...
    
    def clear_cache(self):
        """
        Clear all internal caches, for methods that alter the app registry.

        This is mostly used in tests.
        """
        ...
    
    def lazy_model_operation(self, function, *model_keys):
        """
        Take a function and a number of ("app_label", "modelname") tuples, and
        when all the corresponding models have been imported and registered,
        call the function with the model classes as its arguments.

        The function passed to this method must accept exactly n models as
        arguments, where n=len(model_keys).
        """
        ...
    
    def do_pending_operations(self, model):
        """
        Take a newly-prepared model and pass it to each function waiting for
        it. This is called at the very end of Apps.register_model().
        """
        ...
    


apps = ...