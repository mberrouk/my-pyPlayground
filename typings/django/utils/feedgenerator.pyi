from _typeshed import Incomplete
from django.utils.encoding import iri_to_uri as iri_to_uri
from django.utils.xmlutils import SimplerXMLGenerator as SimplerXMLGenerator

def rfc2822_date(date): ...
def rfc3339_date(date): ...
def get_tag_uri(url, date): ...

class SyndicationFeed:
    feed: Incomplete
    items: Incomplete
    def __init__(self, title, link, description, language: Incomplete | None = None, author_email: Incomplete | None = None, author_name: Incomplete | None = None, author_link: Incomplete | None = None, subtitle: Incomplete | None = None, categories: Incomplete | None = None, feed_url: Incomplete | None = None, feed_copyright: Incomplete | None = None, feed_guid: Incomplete | None = None, ttl: Incomplete | None = None, **kwargs) -> None: ...
    def add_item(self, title, link, description, author_email: Incomplete | None = None, author_name: Incomplete | None = None, author_link: Incomplete | None = None, pubdate: Incomplete | None = None, comments: Incomplete | None = None, unique_id: Incomplete | None = None, unique_id_is_permalink: Incomplete | None = None, categories=(), item_copyright: Incomplete | None = None, ttl: Incomplete | None = None, updateddate: Incomplete | None = None, enclosures: Incomplete | None = None, **kwargs): ...
    def num_items(self): ...
    def root_attributes(self): ...
    def add_root_elements(self, handler) -> None: ...
    def item_attributes(self, item): ...
    def add_item_elements(self, handler, item) -> None: ...
    def write(self, outfile, encoding) -> None: ...
    def writeString(self, encoding): ...
    def latest_post_date(self): ...

class Enclosure:
    url: Incomplete
    def __init__(self, url, length, mime_type) -> None: ...

class RssFeed(SyndicationFeed):
    content_type: str
    def write(self, outfile, encoding) -> None: ...
    def rss_attributes(self): ...
    def write_items(self, handler) -> None: ...
    def add_root_elements(self, handler) -> None: ...
    def endChannelElement(self, handler) -> None: ...

class RssUserland091Feed(RssFeed):
    def add_item_elements(self, handler, item) -> None: ...

class Rss201rev2Feed(RssFeed):
    def add_item_elements(self, handler, item) -> None: ...

class Atom1Feed(SyndicationFeed):
    content_type: str
    ns: str
    def write(self, outfile, encoding) -> None: ...
    def root_attributes(self): ...
    def add_root_elements(self, handler) -> None: ...
    def write_items(self, handler) -> None: ...
    def add_item_elements(self, handler, item) -> None: ...
DefaultFeed = Rss201rev2Feed
