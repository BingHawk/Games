from strategy import Strategy, load_strategies
from game import Round, Move_enum
import random

class Scores: 
    DEFECT_DEFECT = 1
    DEFECT_COOPERATE = 5
    COPERATE_COOPERATE = 3
    COOPERATE_DEFECT = 0

class Game:
    strategies: list[Strategy]
    
    def __init__(self, 
                 n_iterations: int = 5,
                 n_rounds: int = 200,
                 random_std_dev: int = 0,
                 ) -> None:
        self.n_rounds = n_rounds
        self.n_iterations = n_iterations
        self.random_std_dev = random_std_dev
        
        self.strategies =  load_strategies()

    
    def randomize_n_round(self) -> int:
        random_term = random.gauss(mu = 0, sigma = self.random_std_dev)
        return self.n_rounds + round(random_term)
    
    def run(self) -> None:
        for i in range(0, self.n_iterations):
            self.__run_iteration()
    
    def print_scores(self) -> None:
        for strat in self.strategies:  
            print(strat)
    
    def __run_iteration(self) -> None:
        n_rounds = self.randomize_n_round() if self.random_std_dev != 0 else self.n_rounds
            
        strats_run: list[Strategy] = []
        for own_strat in self.strategies:
            strats_run.append(own_strat)
            for opp_strat in strats_run:
                round_history: list[Round] = []
                for _ in range(0, n_rounds):
                    own_move = own_strat.execute(round_history)
                    opp_move = opp_strat.execute(round_history)

                    round_result = Round(
                        opp_move,
                        own_move
                    )
                    round_history.append(round_result)
                    self.__add_scores(own_strat, opp_strat, own_move, opp_move)
                                        
    def __add_scores(self, own_strat:Strategy, opp_strat:Strategy, own_move:Move_enum, opp_move:Move_enum) -> None:
        if own_move == Move_enum.defect:
            if opp_move == Move_enum.defect:
                own_strat.add_to_score(Scores.DEFECT_DEFECT)
                opp_strat.add_to_score(Scores.DEFECT_DEFECT)
            elif opp_move == Move_enum.cooperate: 
                own_strat.add_to_score(Scores.DEFECT_COOPERATE)
                opp_strat.add_to_score(Scores.COOPERATE_DEFECT)
                
        elif own_move == Move_enum.cooperate:
            if opp_move == Move_enum.defect:
                own_strat.add_to_score(Scores.COOPERATE_DEFECT)
                opp_strat.add_to_score(Scores.DEFECT_COOPERATE)
            elif opp_move == Move_enum.cooperate: 
                own_strat.add_to_score(Scores.COPERATE_COOPERATE)
                opp_strat.add_to_score(Scores.COPERATE_COOPERATE)
                            
            
            
                    
