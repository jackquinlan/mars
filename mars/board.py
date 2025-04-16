import numpy as np
from mars.bitboard import Bitboard

VALID_PIECES = ['p', 'n', 'b', 'r', 'q', 'k', # black pieces
                'P', 'N', 'B', 'R', 'Q', 'K'] # white pieces


class Board:
    def __init__(self, fen: str): 
        self.bitboards = self.load_from_fen(fen)
    
    def load_from_fen(self, board: str) -> dict[str, Bitboard]:
        # Example input: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
        bitboards = {
            p: Bitboard(0) for p in VALID_PIECES
        }
        idx = 56 # start index @ A8
        for rank in board.split("/"):
            for char in rank:
                if char.isdigit():
                    idx += int(char)
                else:
                    assert char in VALID_PIECES, "Invalid piece"
                    bitboards[char].set_bit(idx)
                    idx += 1
            idx -= 16 # reset index to next rank
        return bitboards
    
