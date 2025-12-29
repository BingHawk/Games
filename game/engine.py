from strategy import load_strategies
from core import Points, Round, Move_enum, Player
import random


class Game:
    players: list[Player]
    
    def __init__(self, 
                 n_iterations: int = 5,
                 n_rounds: int = 200,
                 random_std_dev: int = 0,
                 points: Points = None
                 ) -> None:
        self.n_rounds = n_rounds
        self.n_iterations = n_iterations
        self.random_std_dev = random_std_dev
        
        strategies = load_strategies()
        self.players = [Player(strat) for strat in strategies]
        self.points = points if points is not None else points()

    
    def randomize_n_round(self) -> int:
        random_term = random.gauss(mu = 0, sigma = self.random_std_dev)
        return self.n_rounds + round(random_term)
    
    def run(self) -> None:
        for _ in range(0, self.n_iterations):
            self.__run_iteration()
    
    def print_points(self) -> None:
        self.players.sort(reverse=True)
        for strat in self.players:  
            print(strat)
    
    def __run_iteration(self) -> None:
        n_rounds = self.randomize_n_round() if self.random_std_dev != 0 else self.n_rounds
            
        players_run: list[Player] = []
        for own_player in self.players:
            players_run.append(own_player)
            for opp_player in players_run:
                round_history: list[Round] = []
                for _ in range(0, n_rounds):
                    own_move = own_player.strategy.execute(round_history)
                    opp_move = opp_player.strategy.execute(round_history)

                    round_result = Round(
                        opp_move,
                        own_move
                    )
                    
                    round_history.append(round_result)
                    self.__add_points(own_player, opp_player, own_move, opp_move)
                                        
    def __add_points(self, own_player:Player, opp_player:Player, own_move:Move_enum, opp_move:Move_enum) -> None:
        if own_move == Move_enum.defect:
            if opp_move == Move_enum.defect:
                own_player.add_to_score(self.points.DEFECT_DEFECT)
                opp_player.add_to_score(self.points.DEFECT_DEFECT)
            elif opp_move == Move_enum.cooperate: 
                own_player.add_to_score(self.points.DEFECT_COOPERATE)
                opp_player.add_to_score(self.points.COOPERATE_DEFECT)
                
        elif own_move == Move_enum.cooperate:
            if opp_move == Move_enum.defect:
                own_player.add_to_score(self.points.COOPERATE_DEFECT)
                opp_player.add_to_score(self.points.DEFECT_COOPERATE)
            elif opp_move == Move_enum.cooperate: 
                own_player.add_to_score(self.points.COPERATE_COOPERATE)
                opp_player.add_to_score(self.points.COPERATE_COOPERATE)
                            
            
            
                    
