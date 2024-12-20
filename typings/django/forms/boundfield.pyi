from _typeshed import Incomplete
from django.forms.utils import RenderableFieldMixin

__all__ = ['BoundField']

class BoundField(RenderableFieldMixin):
    form: Incomplete
    field: Incomplete
    name: Incomplete
    html_name: Incomplete
    html_initial_name: Incomplete
    html_initial_id: Incomplete
    label: Incomplete
    help_text: Incomplete
    renderer: Incomplete
    def __init__(self, form, field, name) -> None: ...
    def subwidgets(self): ...
    def __bool__(self) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, idx): ...
    @property
    def errors(self): ...
    @property
    def template_name(self): ...
    def get_context(self): ...
    def as_widget(self, widget: Incomplete | None = None, attrs: Incomplete | None = None, only_initial: bool = False): ...
    def as_text(self, attrs: Incomplete | None = None, **kwargs): ...
    def as_textarea(self, attrs: Incomplete | None = None, **kwargs): ...
    def as_hidden(self, attrs: Incomplete | None = None, **kwargs): ...
    @property
    def data(self): ...
    def value(self): ...
    def label_tag(self, contents: Incomplete | None = None, attrs: Incomplete | None = None, label_suffix: Incomplete | None = None, tag: Incomplete | None = None): ...
    def legend_tag(self, contents: Incomplete | None = None, attrs: Incomplete | None = None, label_suffix: Incomplete | None = None): ...
    def css_classes(self, extra_classes: Incomplete | None = None): ...
    @property
    def is_hidden(self): ...
    @property
    def auto_id(self): ...
    @property
    def id_for_label(self): ...
    def initial(self): ...
    def build_widget_attrs(self, attrs, widget: Incomplete | None = None): ...
    @property
    def widget_type(self): ...
    @property
    def use_fieldset(self): ...

class BoundWidget:
    parent_widget: Incomplete
    data: Incomplete
    renderer: Incomplete
    def __init__(self, parent_widget, data, renderer) -> None: ...
    def tag(self, wrap_label: bool = False): ...
    @property
    def template_name(self): ...
    @property
    def id_for_label(self): ...
    @property
    def choice_label(self): ...
