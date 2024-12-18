from _typeshed import Incomplete
from django.db.models import CharField as CharField, Expression as Expression, Field as Field, FloatField as FloatField, Func as Func, Lookup as Lookup, TextField as TextField, Value as Value
from django.db.models.expressions import CombinedExpression as CombinedExpression, register_combinable_fields as register_combinable_fields
from django.db.models.functions import Cast as Cast, Coalesce as Coalesce

class SearchVectorExact(Lookup):
    lookup_name: str
    rhs: Incomplete
    def process_rhs(self, qn, connection): ...
    def as_sql(self, qn, connection): ...

class SearchVectorField(Field):
    def db_type(self, connection): ...

class SearchQueryField(Field):
    def db_type(self, connection): ...

class _Float4Field(Field):
    def db_type(self, connection): ...

class SearchConfig(Expression):
    config: Incomplete
    def __init__(self, config) -> None: ...
    @classmethod
    def from_parameter(cls, config): ...
    def get_source_expressions(self): ...
    def set_source_expressions(self, exprs) -> None: ...
    def as_sql(self, compiler, connection): ...

class SearchVectorCombinable:
    ADD: str

class SearchVector(SearchVectorCombinable, Func):
    function: str
    arg_joiner: str
    output_field: Incomplete
    config: Incomplete
    weight: Incomplete
    def __init__(self, *expressions, config: Incomplete | None = None, weight: Incomplete | None = None) -> None: ...
    def resolve_expression(self, query: Incomplete | None = None, allow_joins: bool = True, reuse: Incomplete | None = None, summarize: bool = False, for_save: bool = False): ...
    def as_sql(self, compiler, connection, function: Incomplete | None = None, template: Incomplete | None = None): ...

class CombinedSearchVector(SearchVectorCombinable, CombinedExpression):
    config: Incomplete
    def __init__(self, lhs, connector, rhs, config, output_field: Incomplete | None = None) -> None: ...

class SearchQueryCombinable:
    BITAND: str
    BITOR: str
    def __or__(self, other): ...
    def __ror__(self, other): ...
    def __and__(self, other): ...
    def __rand__(self, other): ...

class SearchQuery(SearchQueryCombinable, Func):
    output_field: Incomplete
    SEARCH_TYPES: Incomplete
    function: Incomplete
    config: Incomplete
    invert: Incomplete
    def __init__(self, value, output_field: Incomplete | None = None, *, config: Incomplete | None = None, invert: bool = False, search_type: str = 'plain') -> None: ...
    def as_sql(self, compiler, connection, function: Incomplete | None = None, template: Incomplete | None = None): ...
    def __invert__(self): ...

class CombinedSearchQuery(SearchQueryCombinable, CombinedExpression):
    config: Incomplete
    def __init__(self, lhs, connector, rhs, config, output_field: Incomplete | None = None) -> None: ...

class SearchRank(Func):
    function: str
    output_field: Incomplete
    def __init__(self, vector, query, weights: Incomplete | None = None, normalization: Incomplete | None = None, cover_density: bool = False) -> None: ...

class SearchHeadline(Func):
    function: str
    template: str
    output_field: Incomplete
    options: Incomplete
    def __init__(self, expression, query, *, config: Incomplete | None = None, start_sel: Incomplete | None = None, stop_sel: Incomplete | None = None, max_words: Incomplete | None = None, min_words: Incomplete | None = None, short_word: Incomplete | None = None, highlight_all: Incomplete | None = None, max_fragments: Incomplete | None = None, fragment_delimiter: Incomplete | None = None) -> None: ...
    def as_sql(self, compiler, connection, function: Incomplete | None = None, template: Incomplete | None = None): ...

class TrigramBase(Func):
    output_field: Incomplete
    def __init__(self, expression, string, **extra) -> None: ...

class TrigramWordBase(Func):
    output_field: Incomplete
    def __init__(self, string, expression, **extra) -> None: ...

class TrigramSimilarity(TrigramBase):
    function: str

class TrigramDistance(TrigramBase):
    function: str
    arg_joiner: str

class TrigramWordDistance(TrigramWordBase):
    function: str
    arg_joiner: str

class TrigramStrictWordDistance(TrigramWordBase):
    function: str
    arg_joiner: str

class TrigramWordSimilarity(TrigramWordBase):
    function: str

class TrigramStrictWordSimilarity(TrigramWordBase):
    function: str
