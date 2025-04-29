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
        # TODO: Finish
        return f"{SQUARES[self.start]}{SQUARES[self.end]}".lower()

class MoveGen:

    piece_attack_sets: dict[str, dict[int, Bitboard]] # { piece: { square: Bitboard } }
    pawn_attacks: dict[str, dict[int, Bitboard]]      # { color: { square: Bitboard } }

    def __init__(self):
        self.pawn_attacks = self._init_pawn_attack_sets()
        self.piece_attack_sets = self._init_attack_sets()

        self.piece_attack_sets["r"][1].pprint()
    
    def pseudo_legal_moves(self, position: Position) -> list[Move]:
        move_list = []

        # Moves that only depend on origin square
        move_list.extend(self.pawn_moves(position))
        move_list.extend(self.king_moves(position))
        move_list.extend(self.knight_moves(position))
        # Moves that depend on origin square & "blockers" (bishops + rooks)
        # Queen moves are calculated as the intersection of rook + bishop moves

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
            attack = self.pawn_attacks[color][square] & enemy_pieces
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
                attack = self.pawn_attacks[color][square]
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
            attack = self.piece_attack_sets["n"][square]
            for end in get_squares_from_bitboard(attack):
                if player.get_bit(end): 
                    # Can't move here because a friendly piece is present
                    continue
                if not enemy.get_bit(end):
                    moves.append(Move(start=square, end=end))
                else:
                    moves.append(Move(start=square, end=end, capture=True))
        return moves 

    def king_moves(self, position: Position) -> list[Move]:
        moves: list[Move] = []
        board = position.board
        color = position.color

        player = board.occupied_by_color(color)
        enemy  = board.occupied_by_color(position.opponent)
        player_king = board.piece_bitboard("K" if color == "w" else "k")
        for square in get_squares_from_bitboard(player_king):
            attack = self.piece_attack_sets["k"][square]
            for end in get_squares_from_bitboard(attack):
                if player.get_bit(end): 
                    # Can't move here because a friendly piece is present
                    continue
                if not enemy.get_bit(end):
                    moves.append(Move(start=square, end=end))
                else:
                    moves.append(Move(start=square, end=end, capture=True))
        return moves
    
    def _init_pawn_attack_sets(self) -> dict[str, dict[int, Bitboard]]:
        pawn_attacks = {}
        for c in VALID_COLORS:
            pawn_attacks[c] = {}
            for s in range(0, 64):
                b = np.uint64(1 << s)
                if c == "w":
                    pawn_attacks[c][s] = Bitboard(((b << 7) & ~H_FILE) | ((b << 9) & ~A_FILE))
                else:
                    pawn_attacks[c][s] = Bitboard(((b >> 7) & ~A_FILE) | ((b >> 9) & ~H_FILE))
        return pawn_attacks

    def _init_attack_sets(self) -> dict[str, dict[int, Bitboard]]:
        attacks = {}
        attacks["k"] = self.king_attack_sets()
        attacks["r"] = self.rook_attack_sets()
        attacks["n"] = self.knight_attack_sets()
        return attacks
    
    def knight_attack_sets(self) -> dict[int, Bitboard]:
        knight_attack = {}
        for s in range(0, 64):
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
    
    def king_attack_sets(self) -> dict[int, Bitboard]:
        king_attack = {}
        for s in range(0, 64):
            b = np.uint64(1 << s)
            king_attack[s] = Bitboard(
                (b << 8) |
                (b >> 8) | 
                (b << 1) & (~A_FILE) |
                (b >> 1) & (~H_FILE) |
                (b >> 9) & (~H_FILE) |
                (b << 9) & (~A_FILE) |
                (b >> 7) & (~A_FILE) |
                (b << 7) & (~H_FILE)
            )
        return king_attack
    
    def rook_attack_sets(self) -> dict[int, Bitboard]:
        rook_attack = {}
        # Generate occupancy masks for rooks for each square on the board. Not accounting for blockers
        for s in range(0, 64):
            b = Bitboard(0)
            f = s % 8       # file
            r = (s - f) / 8 # rank
            for rank in range(0, 8):
                rank_sq = (rank * 8) + f
                if not rank_sq == s:
                    b.set_bit(int(rank_sq))
            for file in range(0, 8):
                file_sq = (r * 8) + file
                if file_sq != s:
                    b.set_bit(int(file_sq))
            rook_attack[s] = b
        return rook_attack

