from .base import Strategy
from .builtin import all_strat_funcs

def load_strategies() -> list[Strategy]:
    return [Strategy(fn) for fn in all_strat_funcs]