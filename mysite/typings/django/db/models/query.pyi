"""
This type stub file was generated by pyright.
"""

from django.db.models.utils import AltersData
from django.utils.functional import cached_property

"""
The main QuerySet implementation. This provides the public API for the ORM.
"""
MAX_GET_RESULTS = ...
REPR_OUTPUT_SIZE = ...
class BaseIterable:
    def __init__(self, queryset, chunked_fetch=..., chunk_size=...) -> None:
        ...
    
    def __aiter__(self): # -> AsyncGenerator[Any, Any]:
        ...
    


class ModelIterable(BaseIterable):
    """Iterable that yields a model instance for each row."""
    def __iter__(self): # -> Generator[Any, Any, None]:
        ...
    


class RawModelIterable(BaseIterable):
    """
    Iterable that yields a model instance for each row from a raw queryset.
    """
    def __iter__(self): # -> Generator[Any, Any, None]:
        ...
    


class ValuesIterable(BaseIterable):
    """
    Iterable returned by QuerySet.values() that yields a dict for each row.
    """
    def __iter__(self): # -> Generator[dict[Any, Any], Any, None]:
        ...
    


class ValuesListIterable(BaseIterable):
    """
    Iterable returned by QuerySet.values_list(flat=False) that yields a tuple
    for each row.
    """
    def __iter__(self): # -> map[Any]:
        ...
    


class NamedValuesListIterable(ValuesListIterable):
    """
    Iterable returned by QuerySet.values_list(named=True) that yields a
    namedtuple for each row.
    """
    def __iter__(self): # -> Generator[Row, Any, None]:
        ...
    


class FlatValuesListIterable(BaseIterable):
    """
    Iterable returned by QuerySet.values_list(flat=True) that yields single
    values.
    """
    def __iter__(self): # -> Generator[Any, Any, None]:
        ...
    


class QuerySet(AltersData):
    """Represent a lazy database lookup for a set of objects."""
    def __init__(self, model=..., query=..., using=..., hints=...) -> None:
        ...
    
    @property
    def query(self): # -> Query:
        ...
    
    @query.setter
    def query(self, value): # -> None:
        ...
    
    def as_manager(cls): # -> Any:
        ...
    
    as_manager = ...
    def __deepcopy__(self, memo): # -> Self:
        """Don't populate the QuerySet's cache."""
        ...
    
    def __getstate__(self): # -> dict[str, Any]:
        ...
    
    def __setstate__(self, state): # -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __iter__(self):
        """
        The queryset iterator protocol uses three nested iterators in the
        default case:
            1. sql.compiler.execute_sql()
               - Returns 100 rows at time (constants.GET_ITERATOR_CHUNK_SIZE)
                 using cursor.fetchmany(). This part is responsible for
                 doing some column masking, and returning the rows in chunks.
            2. sql.compiler.results_iter()
               - Returns one row at time. At this point the rows are still just
                 tuples. In some cases the return values are converted to
                 Python values at this location.
            3. self.iterator()
               - Responsible for turning the rows into model objects.
        """
        ...
    
    def __aiter__(self): # -> AsyncGenerator[dict[Any, Any], Any]:
        ...
    
    def __bool__(self): # -> bool:
        ...
    
    def __getitem__(self, k): # -> dict[Any, Any] | list[dict[Any, Any]] | list[Any] | Self:
        """Retrieve an item or slice from the set of results."""
        ...
    
    def __class_getitem__(cls, *args, **kwargs): # -> type[Self]:
        ...
    
    def __and__(self, other): # -> EmptyQuerySet | <subclass of QuerySet* and EmptyQuerySet> | QuerySet:
        ...
    
    def __or__(self, other): # -> QuerySet:
        ...
    
    def __xor__(self, other): # -> QuerySet:
        ...
    
    def iterator(self, chunk_size=...): # -> Generator[Any | dict[Any, Any], Any, None]:
        """
        An iterator over the results from applying this QuerySet to the
        database. chunk_size must be provided for QuerySets that prefetch
        related objects. Otherwise, a default chunk_size of 2000 is supplied.
        """
        ...
    
    async def aiterator(self, chunk_size=...): # -> Generator[Any, Any, None]:
        """
        An asynchronous iterator over the results from applying this QuerySet
        to the database.
        """
        ...
    
    def aggregate(self, *args, **kwargs):
        """
        Return a dictionary containing the calculations (aggregation)
        over the current queryset.

        If args is present the expression is passed as a kwarg using
        the Aggregate object's default alias.
        """
        ...
    
    async def aaggregate(self, *args, **kwargs):
        ...
    
    def count(self): # -> int:
        """
        Perform a SELECT COUNT() and return the number of records as an
        integer.

        If the QuerySet is already fully cached, return the length of the
        cached results set to avoid multiple SELECT COUNT(*) calls.
        """
        ...
    
    async def acount(self): # -> int:
        ...
    
    def get(self, *args, **kwargs): # -> dict[Any, Any]:
        """
        Perform the query and return a single object matching the given
        keyword arguments.
        """
        ...
    
    async def aget(self, *args, **kwargs): # -> dict[Any, Any]:
        ...
    
    def create(self, **kwargs):
        """
        Create a new object with the given kwargs, saving it to the database
        and returning the created object.
        """
        ...
    
    async def acreate(self, **kwargs):
        ...
    
    def bulk_create(self, objs, batch_size=..., ignore_conflicts=..., update_conflicts=..., update_fields=..., unique_fields=...): # -> list[Any]:
        """
        Insert each of the instances into the database. Do *not* call
        save() on each of the instances, do not send any pre/post_save
        signals, and do not set the primary key attribute if it is an
        autoincrement field (except if features.can_return_rows_from_bulk_insert=True).
        Multi-table models are not supported.
        """
        ...
    
    async def abulk_create(self, objs, batch_size=..., ignore_conflicts=..., update_conflicts=..., update_fields=..., unique_fields=...): # -> list[Any]:
        ...
    
    def bulk_update(self, objs, fields, batch_size=...): # -> Literal[0]:
        """
        Update the given fields in each of the given objects in the database.
        """
        ...
    
    async def abulk_update(self, objs, fields, batch_size=...): # -> int:
        ...
    
    def get_or_create(self, defaults=..., **kwargs): # -> tuple[Any | dict[Any, Any], Literal[False]] | tuple[Any, Literal[True]]:
        """
        Look up an object with the given kwargs, creating one if necessary.
        Return a tuple of (object, created), where created is a boolean
        specifying whether an object was created.
        """
        ...
    
    async def aget_or_create(self, defaults=..., **kwargs): # -> tuple[Any | dict[Any, Any], Literal[False]] | tuple[Any, Literal[True]]:
        ...
    
    def update_or_create(self, defaults=..., create_defaults=..., **kwargs): # -> tuple[Any | dict[Any, Any], Literal[True]] | tuple[Any | dict[Any, Any], Literal[False]]:
        """
        Look up an object with the given kwargs, updating one with defaults
        if it exists, otherwise create a new one. Optionally, an object can
        be created with different values than defaults by using
        create_defaults.
        Return a tuple (object, created), where created is a boolean
        specifying whether an object was created.
        """
        ...
    
    async def aupdate_or_create(self, defaults=..., create_defaults=..., **kwargs): # -> tuple[Any | dict[Any, Any], Literal[True]] | tuple[Any | dict[Any, Any], Literal[False]]:
        ...
    
    def earliest(self, *fields): # -> dict[Any, Any]:
        ...
    
    async def aearliest(self, *fields): # -> dict[Any, Any]:
        ...
    
    def latest(self, *fields): # -> dict[Any, Any]:
        """
        Return the latest object according to fields (if given) or by the
        model's Meta.get_latest_by.
        """
        ...
    
    async def alatest(self, *fields): # -> dict[Any, Any]:
        ...
    
    def first(self): # -> dict[Any, Any] | None:
        """Return the first object of a query or None if no match is found."""
        ...
    
    async def afirst(self): # -> dict[Any, Any] | None:
        ...
    
    def last(self): # -> dict[Any, Any] | None:
        """Return the last object of a query or None if no match is found."""
        ...
    
    async def alast(self): # -> dict[Any, Any] | None:
        ...
    
    def in_bulk(self, id_list=..., *, field_name=...): # -> dict[Any, Any]:
        """
        Return a dictionary mapping each of the given IDs to the object with
        that ID. If `id_list` isn't provided, evaluate the entire QuerySet.
        """
        ...
    
    async def ain_bulk(self, id_list=..., *, field_name=...): # -> dict[Any, Any]:
        ...
    
    def delete(self): # -> tuple[Any | int, dict[Any, Any | int] | dict[Any, int]]:
        """Delete the records in the current QuerySet."""
        ...
    
    async def adelete(self): # -> tuple[Any | int, dict[Any, Any | int] | dict[Any, int]]:
        ...
    
    def update(self, **kwargs):
        """
        Update all elements in the current QuerySet, setting all the given
        fields to the appropriate values.
        """
        ...
    
    async def aupdate(self, **kwargs):
        ...
    
    def exists(self): # -> bool:
        """
        Return True if the QuerySet would have any results, False otherwise.
        """
        ...
    
    async def aexists(self): # -> bool:
        ...
    
    def contains(self, obj): # -> bool:
        """
        Return True if the QuerySet contains the provided obj,
        False otherwise.
        """
        ...
    
    async def acontains(self, obj): # -> bool:
        ...
    
    def explain(self, *, format=..., **options): # -> str:
        """
        Runs an EXPLAIN on the SQL query this QuerySet would perform, and
        returns the results.
        """
        ...
    
    async def aexplain(self, *, format=..., **options): # -> str:
        ...
    
    def raw(self, raw_query, params=..., translations=..., using=...): # -> RawQuerySet:
        ...
    
    def values(self, *fields, **expressions): # -> Self:
        ...
    
    def values_list(self, *fields, flat=..., named=...): # -> Self:
        ...
    
    def dates(self, field_name, kind, order=...): # -> Self:
        """
        Return a list of date objects representing all available dates for
        the given field_name, scoped to 'kind'.
        """
        ...
    
    def datetimes(self, field_name, kind, order=..., tzinfo=...): # -> Self:
        """
        Return a list of datetime objects representing all available
        datetimes for the given field_name, scoped to 'kind'.
        """
        ...
    
    def none(self): # -> Self:
        """Return an empty QuerySet."""
        ...
    
    def all(self): # -> Self:
        """
        Return a new QuerySet that is a copy of the current one. This allows a
        QuerySet to proxy for a model manager in some cases.
        """
        ...
    
    def filter(self, *args, **kwargs): # -> Self:
        """
        Return a new QuerySet instance with the args ANDed to the existing
        set.
        """
        ...
    
    def exclude(self, *args, **kwargs): # -> Self:
        """
        Return a new QuerySet instance with NOT (args) ANDed to the existing
        set.
        """
        ...
    
    def complex_filter(self, filter_obj): # -> Self:
        """
        Return a new QuerySet instance with filter_obj added to the filters.

        filter_obj can be a Q object or a dictionary of keyword lookup
        arguments.

        This exists to support framework features such as 'limit_choices_to',
        and usually it will be more natural to use other methods.
        """
        ...
    
    def union(self, *other_qs, all=...): # -> <subclass of QuerySet* and EmptyQuerySet> | QuerySet:
        ...
    
    def intersection(self, *other_qs): # -> <subclass of QuerySet* and EmptyQuerySet> | EmptyQuerySet | QuerySet:
        ...
    
    def difference(self, *other_qs): # -> <subclass of QuerySet* and EmptyQuerySet> | QuerySet:
        ...
    
    def select_for_update(self, nowait=..., skip_locked=..., of=..., no_key=...): # -> Self:
        """
        Return a new QuerySet instance that will select objects with a
        FOR UPDATE lock.
        """
        ...
    
    def select_related(self, *fields): # -> Self:
        """
        Return a new QuerySet instance that will select related objects.

        If fields are specified, they must be ForeignKey fields and only those
        related objects are included in the selection.

        If select_related(None) is called, clear the list.
        """
        ...
    
    def prefetch_related(self, *lookups): # -> Self:
        """
        Return a new QuerySet instance that will prefetch the specified
        Many-To-One and Many-To-Many related objects when the QuerySet is
        evaluated.

        When prefetch_related() is called more than once, append to the list of
        prefetch lookups. If prefetch_related(None) is called, clear the list.
        """
        ...
    
    def annotate(self, *args, **kwargs): # -> Self:
        """
        Return a query set in which the returned objects have been annotated
        with extra data or aggregations.
        """
        ...
    
    def alias(self, *args, **kwargs): # -> Self:
        """
        Return a query set with added aliases for extra data or aggregations.
        """
        ...
    
    def order_by(self, *field_names): # -> Self:
        """Return a new QuerySet instance with the ordering changed."""
        ...
    
    def distinct(self, *field_names): # -> Self:
        """
        Return a new QuerySet instance that will select only distinct results.
        """
        ...
    
    def extra(self, select=..., where=..., params=..., tables=..., order_by=..., select_params=...): # -> Self:
        """Add extra SQL fragments to the query."""
        ...
    
    def reverse(self): # -> Self:
        """Reverse the ordering of the QuerySet."""
        ...
    
    def defer(self, *fields): # -> Self:
        """
        Defer the loading of data for certain fields until they are accessed.
        Add the set of deferred fields to any existing set of deferred fields.
        The only exception to this is if None is passed in as the only
        parameter, in which case removal all deferrals.
        """
        ...
    
    def only(self, *fields): # -> Self:
        """
        Essentially, the opposite of defer(). Only the fields passed into this
        method and that are not already specified as deferred are loaded
        immediately when the queryset is evaluated.
        """
        ...
    
    def using(self, alias): # -> Self:
        """Select which database this QuerySet should execute against."""
        ...
    
    @property
    def ordered(self): # -> bool:
        """
        Return True if the QuerySet is ordered -- i.e. has an order_by()
        clause or a default ordering on the model (or is empty).
        """
        ...
    
    @property
    def db(self): # -> Any | Literal['default']:
        """Return the database used if this query is executed now."""
        ...
    
    def resolve_expression(self, *args, **kwargs): # -> Empty:
        ...
    


class InstanceCheckMeta(type):
    def __instancecheck__(self, instance): # -> bool:
        ...
    


class EmptyQuerySet(metaclass=InstanceCheckMeta):
    """
    Marker class to checking if a queryset is empty by .none():
        isinstance(qs.none(), EmptyQuerySet) -> True
    """
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class RawQuerySet:
    """
    Provide an iterator which converts the results of raw SQL queries into
    annotated model instances.
    """
    def __init__(self, raw_query, model=..., query=..., params=..., translations=..., using=..., hints=...) -> None:
        ...
    
    def resolve_model_init_order(self): # -> tuple[list[Any], list[Any], list[tuple[Any, int]]]:
        """Resolve the init field names and value positions."""
        ...
    
    def prefetch_related(self, *lookups): # -> Self:
        """Same as QuerySet.prefetch_related()"""
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __bool__(self): # -> bool:
        ...
    
    def __iter__(self):
        ...
    
    def __aiter__(self): # -> AsyncGenerator[Any, Any]:
        ...
    
    def iterator(self): # -> Generator[Any, Any, None]:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __getitem__(self, k):
        ...
    
    @property
    def db(self): # -> Any | Literal['default']:
        """Return the database used if this query is executed now."""
        ...
    
    def using(self, alias): # -> RawQuerySet:
        """Select the database this RawQuerySet should execute against."""
        ...
    
    @cached_property
    def columns(self): # -> list[Any]:
        """
        A list of model field names in the order they'll appear in the
        query results.
        """
        ...
    
    @cached_property
    def model_fields(self): # -> dict[Any, Any]:
        """A dict mapping column names to model field names."""
        ...
    


class Prefetch:
    def __init__(self, lookup, queryset=..., to_attr=...) -> None:
        ...
    
    def __getstate__(self): # -> dict[str, Any]:
        ...
    
    def add_prefix(self, prefix): # -> None:
        ...
    
    def get_current_prefetch_to(self, level): # -> str:
        ...
    
    def get_current_to_attr(self, level): # -> tuple[Any, Any | None]:
        ...
    
    def get_current_queryset(self, level): # -> None:
        ...
    
    def get_current_querysets(self, level): # -> list[Any] | None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


def normalize_prefetch_lookups(lookups, prefix=...): # -> list[Any]:
    """Normalize lookups into Prefetch objects."""
    ...

def prefetch_related_objects(model_instances, *related_lookups): # -> None:
    """
    Populate prefetched object caches for a list of model instances based on
    the lookups/Prefetch instances given.
    """
    ...

async def aprefetch_related_objects(model_instances, *related_lookups): # -> None:
    """See prefetch_related_objects()."""
    ...

def get_prefetcher(instance, through_attr, to_attr): # -> tuple[Any | None, Any | None, bool, Callable[..., bool] | Any]:
    """
    For the attribute 'through_attr' on the given instance, find
    an object that has a get_prefetch_querysets().
    Return a 4 tuple containing:
    (the object with get_prefetch_querysets (or None),
     the descriptor object representing this relationship (or None),
     a boolean that is False if the attribute was not found at all,
     a function that takes an instance and returns a boolean that is True if
     the attribute has already been fetched for that instance)
    """
    ...

def prefetch_one_level(instances, prefetcher, lookup, level): # -> tuple[list[Any], list[Any]]:
    """
    Helper function for prefetch_related_objects().

    Run prefetches on all instances using the prefetcher object,
    assigning results to relevant caches in instance.

    Return the prefetched objects along with any additional prefetches that
    must be done due to prefetch_related lookups found from default managers.
    """
    ...

class RelatedPopulator:
    """
    RelatedPopulator is used for select_related() object instantiation.

    The idea is that each select_related() model will be populated by a
    different RelatedPopulator instance. The RelatedPopulator instances get
    klass_info and select (computed in SQLCompiler) plus the used db as
    input for initialization. That data is used to compute which columns
    to use, how to instantiate the model, and how to populate the links
    between the objects.

    The actual creation of the objects is done in populate() method. This
    method gets row and from_obj as input and populates the select_related()
    model instance.
    """
    def __init__(self, klass_info, select, db) -> None:
        ...
    
    def populate(self, row, from_obj): # -> None:
        ...
    


def get_related_populators(klass_info, select, db): # -> list[Any]:
    ...

