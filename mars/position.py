from dataclasses import dataclass
from mars.board  import Board

DEFAULT_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


@dataclass
class Position:
    board: Board
    color: str
    castling_rights: str
    en_passant: str
    halfmove_clock: int
    fullmove_count: int

    @classmethod
    def load_from_fen(cls, fen: str=DEFAULT_FEN):
        fen_parts = fen.split(" ")
        return cls(
            board=Board(fen=fen_parts[0]),
            color=fen_parts[1],
            castling_rights=fen_parts[2],
            en_passant=fen_parts[3],
            halfmove_clock=int(fen_parts[4]),
            fullmove_count=int(fen_parts[5]),
        )

