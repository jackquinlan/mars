from mars.game import Game

def main():

    # game = Game(initial_fen="rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq e6 0 1")
    # game = Game(initial_fen="8/P7/8/8/8/8/7p/4k2K w - - 0 1")

    # game = Game(initial_fen="rnbqkbnr/ppp1p1pp/8/3pPp2/8/8/PPPP1PPP/RNBQKBNR w KQkq f6 0 1")
    # game = Game(initial_fen="1b4k1/2P5/5p1p/6p1/8/7P/6P1/6K1 w - - 0 1")

    game = Game(initial_fen="8/7k/7b/1n1P4/8/2N5/8/4K3 w - - 0 1")
    game.loop()

if __name__ == '__main__':
    main()

