from game import Game, Scores

if __name__ == '__main__':
    game = Game(n_iterations=5, n_rounds=200, random_std_dev=5, scores=Scores(1, 5, 3, 0))
    game.run()
    game.print_scores()
    