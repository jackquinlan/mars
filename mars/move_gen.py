import numpy as np
from dataclasses import dataclass
from typing import Optional
from mars.bitboard import Bitboard
from mars.position import Position
from mars.utils import get_squares_from_bitboard, algebraic_to_square_index
from mars import RANK_1, RANK_4, RANK_5, RANK_8, PROMO_PIECES, SQUARES, VALID_COLORS, A_FILE, B_FILE, G_FILE, H_FILE


@dataclass(frozen=True)
class Move:
    start: int 
    end: int   

    # Special cases
    double_push: bool = False
    castle: bool = False
    promotion: Optional[str] = None # Q, R, B, or N
    capture: bool = False
    en_passant: bool = False
    
    def to_algebraic(self):
        # Return the Move in algebraic notation
        alg = f"{SQUARES[self.start]}{SQUARES[self.end]}".lower()
        return alg 

class MoveGen:

    # { color: { piece: { square: Bitboard } } }
    attack_sets: dict[str, dict[str, dict[int, Bitboard]]]
    def __init__(self):
        self.attack_sets = self.generate_attack_sets()
    
    def pseudo_legal_moves(self, position: Position) -> list[Move]:
        move_list = []

        pawn_list = self.pawn_moves(position)
        knight_list = self.knight_moves(position)
        bishop_list = self.bishop_moves(position)

        move_list.extend(pawn_list)
        move_list.extend(knight_list)
        return move_list

    def pawn_moves(self, position: Position) -> list[Move]:
        moves: list[Move] = []
        board = position.board
        color = position.color
        direction = 8 if color == "w" else -8
        promotion_rank = RANK_8 if color == "w" else RANK_1

        # Single and double pushes
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
        player_pawns = board.piece_bitboard("P" if color == "w" else "p")
        enemy_pieces = board.occupied_by_color(position.opponent)
        for square in get_squares_from_bitboard(player_pawns):
            attack = self.attack_sets[color]["p"][square] & enemy_pieces
            for end in get_squares_from_bitboard(attack):
                if (1 << end) & promotion_rank:
                    for promo in PROMO_PIECES:
                        moves.append(Move(start=square, end=end, promotion=promo, capture=True))
                    continue
                moves.append(Move(start=square, end=end, capture=True))

        # En Passant
        if position.en_passant:
            en_passant_index = algebraic_to_square_index(position.en_passant)
            for square in get_squares_from_bitboard(player_pawns):
                attack = self.attack_sets[color]["p"][square]
                if attack.get_bit(en_passant_index):
                    moves.append(Move(start=square, end=en_passant_index, en_passant=True))

        return moves

    def knight_moves(self, position: Position) -> list[Move]:
        moves: list[Move] = []
        board = position.board
        color = position.color
        
        player = board.occupied_by_color(color)
        enemy  = board.occupied_by_color(position.opponent)
        player_knights = board.piece_bitboard("N" if color == "w" else "n")
        for square in get_squares_from_bitboard(player_knights):
            attack = self.attack_sets[color]["n"][square]
            for end in get_squares_from_bitboard(attack):
                if player.get_bit(end): 
                    # Can't move here because a friendly piece is present
                    continue
                if not enemy.get_bit(end):
                    moves.append(Move(start=square, end=end))
                else:
                    moves.append(Move(start=square, end=end, capture=True))
        return moves 

    def bishop_moves(self, position: Position) -> list[Move]:
        moves: list[Move] = []
        board = position.board
        color = position.color

        return moves
    
    def generate_attack_sets(self) -> dict[str, dict[str, dict[int, Bitboard]]]:
        attack = {}
        for c in VALID_COLORS:
            attack[c] = {}
            attack[c]["p"] = self.pawn_attack_sets(color=c)
            attack[c]["n"] = self.knight_attack_sets()
        return attack
    
    def pawn_attack_sets(self, color: str) -> dict[int, Bitboard]:
        pawn_attack = {}
        for s in range(0, 64):
            b = np.uint64(1 << s)
            if color == "w":
                pawn_attack[s] = Bitboard(((b << 7) & ~H_FILE) | ((b << 9) & ~A_FILE))
            else:
                pawn_attack[s] = Bitboard(((b >> 7) & ~A_FILE) | ((b >> 9) & ~H_FILE))
        return pawn_attack

    def knight_attack_sets(self):
        knight_attack = {}
        for s in range(0, 63):
            b = np.uint64(1 << s)
            knight_attack[s] = Bitboard(
                (b << 17) & (~A_FILE)           |
                (b << 10) & (~A_FILE & ~B_FILE) |
                (b << 15) & (~H_FILE)           |
                (b << 6)  & (~G_FILE & ~H_FILE) |
                (b >> 10) & (~G_FILE & ~H_FILE) |
                (b >> 17) & (~H_FILE)           |
                (b >> 15) & (~A_FILE)           |
                (b >> 6)  & (~A_FILE & ~B_FILE)
            )
        return knight_attack

















































