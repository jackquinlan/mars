from mars.bitboard import Bitboard
from mars.position import Position
from mars.game import Game

def main():
    # position = Position.load_from_fen(fen="8/1KP4k/4NP1P/b4qn1/5p1P/2p3rb/N7/2Q5 w - - 0 1")
    # position = Position.load_from_fen(fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    # position.board.piece_bitboard("p").shift_south().pprint()

    # game = Game(initial_fen="rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq e6 0 1")
    game = Game(initial_fen="8/P7/8/8/8/8/7p/4k2K w - - 0 1")
    game.loop()
    return

if __name__ == '__main__':
    main()

