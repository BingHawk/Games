from .strategy import Strategy
from .strategies import all_strat_funcs

def load_strategies() -> list[Strategy]:
    return [Strategy(fn) for fn in all_strat_funcs]