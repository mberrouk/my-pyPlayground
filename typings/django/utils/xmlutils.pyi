from _typeshed import Incomplete
from xml.sax.saxutils import XMLGenerator

class UnserializableContentError(ValueError): ...

class SimplerXMLGenerator(XMLGenerator):
    def addQuickElement(self, name, contents: Incomplete | None = None, attrs: Incomplete | None = None) -> None: ...
    def characters(self, content) -> None: ...
    def startElement(self, name, attrs) -> None: ...
