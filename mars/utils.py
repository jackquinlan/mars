import numpy as np
from mars.bitboard import Bitboard

def get_squares_from_bitboard(bitboard: Bitboard):
    # Yield square indices from a bitboard
    board = int(bitboard.board)
    while board:
        lsb = board & -board
        yield lsb.bit_length() - 1
        board &= board - 1

