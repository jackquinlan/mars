import numpy as np
from mars.bitboard import Bitboard
from mars import VALID_PIECES


class Board:
    def __init__(self, fen: str): 
        self.bitboards = self._load_from_fen(fen)

    @property
    def to_fen(self):
        fen = ""
        return fen

    def occupied(self):
        oc = Bitboard(0)
        for bb in self.bitboards:
            oc |= self.bitboards[bb]
        return oc 
    
    def occupied_by_color(self, color: str):
        assert color in ["w", "b"], "Invalid color"
        # White pieces are represented by uppercase characters
        pieces = ["P", "N", "B", "R", "Q", "K"] if color == "w" else \
                 ["p", "n", "b", "r", "q", "k"]
        oc = Bitboard(0)
        for bb in self.bitboards:
            if bb in pieces: 
                oc |= self.bitboards[bb]
        return oc

    def empty(self):
        return Bitboard(~self.occupied().board) & Bitboard(0xFFFFFFFFFFFFFFFF)
    
    def piece_bitboard(self, piece: str):
        assert piece in VALID_PIECES, "Invalid piece"
        return self.bitboards[piece]

    def _load_from_fen(self, board: str) -> dict[str, Bitboard]:
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
    
