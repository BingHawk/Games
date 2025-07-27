from strategy import Strategy, load_strategies
from game import Round

class Game:
    strategies: list[Strategy] = load_strategies()
    
    def __init__(self, 
                 n_iterations: int = 5,
                 n_rounds: int = 200,
                 is_n_rounds_random: bool = False,
                 ) -> None:
        self.n_rounds = n_rounds
        self.n_iterations = n_iterations
        self.is_n_rounds_random = is_n_rounds_random
    
    def randomize_n_round(self) -> int:
        # disturb the input number of rounds with a random term
        return self.n_rounds
    
    def run(self) -> None:
        for _ in range(0, self.n_iterations):
            self.__run_iteration()
    
    
    def __run_iteration(self) -> None:
        n_rounds = self.randomize_round() if self.is_n_rounds_random else self.n_rounds
            
        strats_run: list[Strategy] = []
        for own_strat in self.strategies:
            strats_run.append(own_strat)
            round_history: list[Round] = []
            for opp_strat in strats_run:
                for _ in range(0, n_rounds):
                    round_result = Round(
                        opp_strat.execute(round_history),
                        own_strat.execute(round_history)
                    )
                    round_history.append(round_result)
            
            # score round history
            
                    
