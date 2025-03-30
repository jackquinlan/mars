from engine.board import Board
from engine.bitboards import Bitboard
from engine.constants import NOT_A_FILE, NOT_H_FILE, RANK_4, RANK_5


class MoveGen:
  def __init__(self, board: Board):
    self.board = board

  def pseudo_legal_moves(self):
    moves = []

  def double_push_pawn_targets(self):
    single_push = self.single_push_pawn_targets()
    if self.board.current_color == 'w':
      return Bitboard(self.shift_north(single_push).bb & self.board.empty.bb & RANK_4)
    else:
      return Bitboard(self.shift_south(single_push).bb & self.board.empty.bb & RANK_5)

  def single_push_pawn_targets(self):
    if self.board.current_color == 'w':
      return Bitboard(self.shift_north(self.board.bbs['P']).bb & self.board.empty.bb)
    else:
      return Bitboard(self.shift_south(self.board.bbs['p']).bb & self.board.empty.bb)

  """
  Compass rose shift operations
  Mainly used to generate attack and move-target sets.

  northwest    north   northeast
  noWe         nort         noEa
           +7    +8    +9
               \  |  /
  west     -1 <-  0 -> +1   east
               /  |  \
           -9    -8    -7
  soWe         sout         soEa
  southwest    south   southeast
  """
  def shift_north(self, bitboard: Bitboard): return Bitboard(bitboard.bb << 8)
  def shift_south(self, bitboard: Bitboard): return Bitboard(bitboard.bb >> 8)
  # Mask off the A and H files by taking the intersection with NOT_A_FILE and NOT_H_FILE
  # This prevents wrapping for non-vertical shifts
  def shift_east(self, bitboard: Bitboard): return Bitboard((bitboard.bb << 1) & NOT_A_FILE)
  def shift_west(self, bitboard: Bitboard): return Bitboard((bitboard.bb >> 1) & NOT_H_FILE)
  def shift_north_east(self, bitboard: Bitboard): return Bitboard((bitboard.bb << 9) & NOT_A_FILE)
  def shift_north_west(self, bitboard: Bitboard): return Bitboard((bitboard.bb << 7) & NOT_H_FILE)
  def shift_south_east(self, bitboard: Bitboard): return Bitboard((bitboard.bb >> 7) & NOT_A_FILE)
  def shift_south_west(self, bitboard: Bitboard): return Bitboard((bitboard.bb >> 9) & NOT_H_FILE)
