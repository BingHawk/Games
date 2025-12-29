from game import Game
from core import Points

if __name__ == '__main__':
    game = Game(n_iterations=5, n_rounds=200, random_std_dev=5, points=Points(1, 5, 3, 0))
    game.run()
    game.print_points()
    
    
    
    