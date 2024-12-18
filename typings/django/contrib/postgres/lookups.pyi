from .search import SearchVector as SearchVector, SearchVectorExact as SearchVectorExact, SearchVectorField as SearchVectorField
from _typeshed import Incomplete
from django.db.models import Transform as Transform
from django.db.models.lookups import PostgresOperatorLookup as PostgresOperatorLookup
from django.db.models.sql.query import Query as Query

class DataContains(PostgresOperatorLookup):
    lookup_name: str
    postgres_operator: str

class ContainedBy(PostgresOperatorLookup):
    lookup_name: str
    postgres_operator: str

class Overlap(PostgresOperatorLookup):
    lookup_name: str
    postgres_operator: str
    rhs: Incomplete
    def get_prep_lookup(self): ...

class HasKey(PostgresOperatorLookup):
    lookup_name: str
    postgres_operator: str
    prepare_rhs: bool

class HasKeys(PostgresOperatorLookup):
    lookup_name: str
    postgres_operator: str
    def get_prep_lookup(self): ...

class HasAnyKeys(HasKeys):
    lookup_name: str
    postgres_operator: str

class Unaccent(Transform):
    bilateral: bool
    lookup_name: str
    function: str

class SearchLookup(SearchVectorExact):
    lookup_name: str
    lhs: Incomplete
    def process_lhs(self, qn, connection): ...

class TrigramSimilar(PostgresOperatorLookup):
    lookup_name: str
    postgres_operator: str

class TrigramWordSimilar(PostgresOperatorLookup):
    lookup_name: str
    postgres_operator: str

class TrigramStrictWordSimilar(PostgresOperatorLookup):
    lookup_name: str
    postgres_operator: str
