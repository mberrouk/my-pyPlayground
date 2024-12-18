from _typeshed import Incomplete

color_names: Incomplete
foreground: Incomplete
background: Incomplete
RESET: str
opt_dict: Incomplete

def colorize(text: str = '', opts=(), **kwargs): ...
def make_style(opts=(), **kwargs): ...

NOCOLOR_PALETTE: str
DARK_PALETTE: str
LIGHT_PALETTE: str
PALETTES: Incomplete
DEFAULT_PALETTE = DARK_PALETTE

def parse_color_setting(config_string): ...
