from _collections_abc import Callable
from game import Move_enum, Round

class Strategy:
    score: int = 0
    strategy_fn: Callable[[Round], Move_enum]
    name: str
    
    def __init__(self, strategy_fn: Callable[[Round], Move_enum]) -> None:
        self.strategy_fn = strategy_fn
        self.name = strategy_fn.__name__
        
    def __str__(self) -> str:
        return f"Strategy {self.name}: {self.score}"
    
    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self,other):
        return self.score < other.score 
    
    def execute(self, history: list[Round]) -> Move_enum:
        move = self.strategy_fn(history)
        return move
    
    def add_to_score(self, score: int) -> None:
        self.score += score
    
