"""
This type stub file was generated by pyright.
"""

from django.db import models

class ContentTypeManager(models.Manager):
    use_in_migrations = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def get_by_natural_key(self, app_label, model): # -> Any:
        ...
    
    def get_for_model(self, model, for_concrete_model=...): # -> Any:
        """
        Return the ContentType object for a given model, creating the
        ContentType if necessary. Lookups are cached so that subsequent lookups
        for the same model don't hit the database.
        """
        ...
    
    def get_for_models(self, *models, for_concrete_models=...): # -> dict[Any, Any]:
        """
        Given *models, return a dictionary mapping {model: content_type}.
        """
        ...
    
    def get_for_id(self, id): # -> Any:
        """
        Lookup a ContentType by ID. Use the same shared cache as get_for_model
        (though ContentTypes are not created on-the-fly by get_by_id).
        """
        ...
    
    def clear_cache(self): # -> None:
        """
        Clear out the content-type cache.
        """
        ...
    


class ContentType(models.Model):
    app_label = ...
    model = ...
    objects = ...
    class Meta:
        verbose_name = ...
        verbose_name_plural = ...
        db_table = ...
        unique_together = ...
    
    
    def __str__(self) -> str:
        ...
    
    @property
    def name(self): # -> CharField | str:
        ...
    
    @property
    def app_labeled_name(self): # -> CharField | LiteralString:
        ...
    
    def model_class(self): # -> None:
        """Return the model class for this type of content."""
        ...
    
    def get_object_for_this_type(self, using=..., **kwargs):
        """
        Return an object of this type for the keyword arguments given.
        Basically, this is a proxy around this object_type's get_object() model
        method. The ObjectNotExist exception, if thrown, will not be caught,
        so code that calls this method should catch it.
        """
        ...
    
    def get_all_objects_for_this_type(self, **kwargs):
        """
        Return all objects of this type for the keyword arguments given.
        """
        ...
    
    def natural_key(self): # -> tuple[CharField, CharField]:
        ...
    

