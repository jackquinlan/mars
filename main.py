from mars.bitboard import Bitboard
from mars.position import Position

def main():
    bitboard = Bitboard(0)
    bitboard.set_bit(3) # set D1

    position = Position.load_from_fen(fen="8/1KP4k/4NP1P/b4qn1/5p1P/2p3rb/N7/2Q5 w - - 0 1")
    position.board.bitboards['N'].pprint()
    return

if __name__ == '__main__':
    main()
