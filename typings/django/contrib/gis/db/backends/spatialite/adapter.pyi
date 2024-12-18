from django.contrib.gis.db.backends.base.adapter import WKTAdapter as WKTAdapter
from django.db.backends.sqlite3.base import Database as Database

class SpatiaLiteAdapter(WKTAdapter):
    def __conform__(self, protocol): ...
