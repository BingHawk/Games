from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from strategy import Strategy


class Player:
    strategy: Strategy
    score: int
    name: str
    strategy_name: str
    
    def __init__(self, strategy: Strategy, name: str | None = None):
        self.strategy = strategy
        self.strategy_name = strategy.name
        self.score = 0
        self.name = name if name is not None else strategy.name
    
    def add_to_score(self, points_to_add: int):
        self.score += points_to_add
        
    def __str__(self):
        return f'{self.name} ({self.strategy_name}): {self.score}'
    
    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self,other):
        return self.score < other.score 