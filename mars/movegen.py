from dataclasses import dataclass
from typing import Optional
from mars.bitboard import Bitboard
from mars.position import Position
from mars.utils import get_squares_from_bitboard
from mars import RANK_1, RANK_4, RANK_5, RANK_8, PROMO_PIECES


@dataclass(frozen=True)
class Move:
    start: int 
    end: int   
    # Special cases
    double_push: bool = False
    promotion: Optional[str] = None # Q, R, B, or N
    
    def __str__(self):
        return f"{self.start} - {self.end}: Double: {self.double_push}, Promo: {self.promotion}"

class MoveGen:
    def __init__(self):
        # Pre-compute attack sets
        # self._pre_compute_attack_sets()
        return
    
    def pseudo_legal_moves(self, position: Position) -> list[Move]:
        move_list = []
        pawn_list = self.pawn_moves(position)

        move_list.extend(pawn_list)
        return move_list

    def pawn_moves(self, position: Position) -> list[Move]:
        moves: list[Move] = []
        board = position.board
        color = position.color
        direction = 8 if color == "w" else -8
        promotion_rank = RANK_8 if color == "w" else RANK_1

        # Single and double pushes
        # TODO: Promotions
        if color == "w":
            single_pushes = board.piece_bitboard("P").shift_north() & board.empty()
        else:
            single_pushes = board.piece_bitboard("p").shift_south() & board.empty()

        for end in get_squares_from_bitboard(single_pushes):
            start = end - direction
            if (1 << end) & promotion_rank:
                for promo in PROMO_PIECES:
                    moves.append(Move(start=start, end=end, promotion=promo))
                continue
            moves.append(Move(start=start, end=end))

        if color == "w":
            double_pushes = single_pushes.shift_north() & board.empty() & Bitboard(RANK_4)
        else:
            double_pushes = single_pushes.shift_south() & board.empty() & Bitboard(RANK_5)

        for end in get_squares_from_bitboard(double_pushes):
            start = end - 2 * direction
            moves.append(Move(start=start,end=end, double_push=True))

        # Captures 
        # En Passant
        return moves
    
