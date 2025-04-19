from mars.bitboard import Bitboard
from mars import SQUARES

def get_squares_from_bitboard(bitboard: Bitboard):
    # Yield square indices from a bitboard
    board = int(bitboard.board)
    while board:
        lsb = board & -board
        yield lsb.bit_length() - 1
        board &= board - 1

def algebraic_to_square_index(square: str) -> int:
    # Convert algebraic (A1) to index (0)
    assert square.upper() in SQUARES, "Invalid square code"
    return SQUARES.index(square.upper())

