from dataclasses import dataclass
from typing import Optional
from mars.board import Board
from mars import DEFAULT_FEN


@dataclass
class Position:
    board: Board
    color: str
    castling_rights: str
    halfmove_clock: int
    fullmove_count: int
    en_passant: Optional[str] = None # En passant square in algebraic notation (e.g., "A2")

    @classmethod
    def load_from_fen(cls, fen: str=DEFAULT_FEN):
        fen_parts = fen.split(" ")
        assert len(fen_parts) == 6, "Fen string must contain 6 parts"
        return cls(
            board=Board(fen=fen_parts[0]),
            color=fen_parts[1],
            castling_rights=fen_parts[2],
            en_passant=fen_parts[3] if fen_parts[3] != "-" else None,
            halfmove_clock=int(fen_parts[4]),
            fullmove_count=int(fen_parts[5]),
        )
    
    @property
    def to_fen(self):
        return " ".join([
            self.board.to_fen,
            self.color,
            self.castling_rights,
            self.en_passant if self.en_passant != None else "-",
            str(self.halfmove_clock),
            str(self.fullmove_count)
        ])

    @property
    def opponent(self):
        return "w" if self.color == "b" else "b"
    
    def make_move(self):
        return

    def checking_pieces(self):
        # Return the pieces that have the king in check
        return

