from engine.board import Board
from engine.bitboards import Bitboard
from engine.constants import NOT_A_FILE, NOT_H_FILE


class MoveGen:
  def __init__(self, board: Board):
    self.board = board

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
  def shift_north(self, bitboard: Bitboard): return bitboard.bb << 8
  def shift_south(self, bitboard: Bitboard): return bitboard.bb >> 8
  # Mask off the A and H files by taking the intersection with NOT_A_FILE and NOT_H_FILE
  # This prevents wrapping for non-vertical shifts
  def shift_east(self, bitboard: Bitboard): return (bitboard.bb << 1) & NOT_A_FILE
  def shift_west(self, bitboard: Bitboard): return (bitboard.bb >> 1) & NOT_H_FILE
  def shift_north_east(self, bitboard: Bitboard): return (bitboard.bb << 9) & NOT_A_FILE
  def shift_north_west(self, bitboard: Bitboard): return (bitboard.bb << 7) & NOT_H_FILE
  def shift_south_east(self, bitboard: Bitboard): return (bitboard.bb >> 7) & NOT_A_FILE
  def shift_south_west(self, bitboard: Bitboard): return (bitboard.bb >> 9) & NOT_H_FILE