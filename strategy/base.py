print(f'{__name__}')
from _collections_abc import Callable
from core import Round, Move_enum

class Strategy:
    strategy_fn: Callable[[Round], Move_enum]
    name: str
    
    def __init__(self, strategy_fn: Callable[[Round], Move_enum]) -> None:
        self.strategy_fn = strategy_fn
        self.name = strategy_fn.__name__
        
    def __str__(self) -> str:
        return f"Strategy {self.name}"
    
    def execute(self, history: list[Round]) -> Move_enum:
        move = self.strategy_fn(history)
        return move
    
