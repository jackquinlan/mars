import numpy as np


class Bitboard:
  """
  A bitboard is a 64-bit integer representing the state of a chessboard. In this case, for a specific piece-type color combination
  A one-bit represents an occupied square, while a zero-bit represents an unoccupied square. 
  
  Uses little endian represetation which maps: Rank 1 .. Rank 8 -> 0..7 and A-File .. H-File -> 0..7
  """
  def __init__(self,
               bb: np.int64):
    assert isinstance(bb, np.int64), "Value must be of type int64"
    self.bb = bb

  @property
  def is_empty(self): return self.bb == 0

  """
  Bit manipulation operations
  """
  def set_bit(self, square: int) -> None:
    """
    mask = (1 << square) = 1{#0's = square}
    mask | self.bb will set the bit at the square to 1. 
    
    example:
    (1 << 2) = 100
    self.bb  = 1010
    self.bb | (1 << square) = 1010 | 0100 = 1110
    """
    assert 0 <= square < 64, "Square must be between 0 and 63"
    self.bb |= (1 << square)
  
  def get_bit(self, square: int) -> bool:
    """
    mask = (1 << square) = 1{#0's = square}
    (1 << square) & self.bb will return non-zero if the bit is set, otherwise will be zero.

    example:
    (1 << 3) = 1000
    self.bb  = 1010
    self.bb & (1 << square) = 1010 & 1000 = 992 (which is non-zero)
    """
    assert 0 <= square < 64, "Square must be between 0 and 63"
    return (self.bb & (1 << square)) != 0

  def clr_bit(self, square: int) -> None:
    """
    mask = ~(1 << square) = 1{#0's = square}
    ~ operator flips all bits in the bitboard: 1000 becomes 0111 

    example:
    (1 << 2) = 1000
    self.bb  = 1010
    self.bb & ~(1 << square) = 1010 & 0111 = 0010
    """
    assert 0 <= square < 64, "Square must be between 0 and 63"
    self.bb &= ~(1 << square)

  def pprint(self):
    """
    Pretty print the bitboard into an 8x8 grid
    """
    # TODO
    return 
