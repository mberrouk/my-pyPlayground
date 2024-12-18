import ipaddress
from _typeshed import Incomplete
from enum import IntEnum
from psycopg import IsolationLevel as IsolationLevel
from psycopg.types.datetime import TimestamptzLoader
from psycopg.types.json import Jsonb as Jsonb
from psycopg.types.range import RangeDumper
from psycopg2 import errors as errors
from psycopg2.extras import Json, Range

Inet = ipaddress.ip_address
DateRange = Range
DateTimeRange = Range
DateTimeTZRange = Range
NumericRange = Range
RANGE_TYPES: Incomplete
TSRANGE_OID: Incomplete
TSTZRANGE_OID: Incomplete

def mogrify(sql, params, connection): ...

class BaseTzLoader(TimestamptzLoader):
    timezone: Incomplete
    def load(self, data): ...

def register_tzloader(tz, context) -> None: ...

class DjangoRangeDumper(RangeDumper):
    def upgrade(self, obj, format): ...

def get_adapters_template(use_tz, timezone): ...

is_psycopg3: bool

class IsolationLevel(IntEnum):
    READ_UNCOMMITTED = ...
    READ_COMMITTED = ...
    REPEATABLE_READ = ...
    SERIALIZABLE = ...

class Jsonb(Json):
    def getquoted(self): ...
