import numpy as np


class Bitboard:
    def __init__(self, board: np.uint64):
        # Force np.uint64 type to avoid future casting issues
        self.board = board if isinstance(board, np.uint64) else np.uint64(board)
    
    def get_bit(self, square: int) -> bool:
        assert 0 <= square < 64, "Square must be 0-63"
        # True if 1, False if 0
        return ((1 << square) & self.board) > 0

    def set_bit(self, square: int):
        assert 0 <= square < 64, "Square must be 0-63"
        self.board |= (1 << square)

    def pprint(self):
        # Print a "pretty" version of the Bitboard. Useful for debugging.
        board_str = ""
        for rank in range(7, -1, -1):
            row = f"{rank+1} "
            for file in range(0, 8):
                row += "1 " if self.get_bit((rank * 8) + file) else "0 "
            board_str += row.rstrip() + "\n"
        board_str += "  A B C D E F G H"
        print(board_str)
                
    def __eq__(self, other):
        assert isinstance(other, Bitboard), "Must be Bitboard type"
        return self.board == other.board

    def __or__(self, other):
        assert isinstance(other, Bitboard), "Must be Bitboard type"
        return Bitboard(self.board | other.board)

    def __xor__(self, other):
        assert isinstance(other, Bitboard), "Must be Bitboard type"
        return Bitboard(self.board ^ other.board)

    def __and__(self, other):
        assert isinstance(other, Bitboard), "Must be Bitboard type"
        return Bitboard(self.board & other.board)

