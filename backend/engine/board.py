import numpy as np
from engine.bitboards import Bitboard
from engine.constants import PIECES


class Board:
  def __init__(self, 
               current_color: str = 'w'):
    self.current_color = current_color
    self.bbs: dict[str, Bitboard] = {
      'P': Bitboard(np.uint64(0x000000000000FF00)), 
      'N': Bitboard(np.uint64(0x0000000000000042)),
      'B': Bitboard(np.uint64(0x0000000000000024)),
      'R': Bitboard(np.uint64(0x0000000000000081)),
      'Q': Bitboard(np.uint64(0x0000000000000008)),
      'K': Bitboard(np.uint64(0x0000000000000010)),
      'p': Bitboard(np.uint64(0x00FF000000000000)),
      'n': Bitboard(np.uint64(0x4200000000000000)),
      'b': Bitboard(np.uint64(0x2400000000000000)),
      'r': Bitboard(np.uint64(0x8100000000000000)),
      'q': Bitboard(np.uint64(0x0800000000000000)),
      'k': Bitboard(np.uint64(0x1000000000000000)),
    }

  @property
  def occupied(self) -> Bitboard:
    o = np.uint64(0)
    for piece in self.bbs.values():
      o |= piece.bb 
    return Bitboard(o)

  @property
  def empty(self) -> Bitboard:
    return Bitboard(~self.occupied.bb)

  @property
  def white_pieces(self) -> Bitboard:
    return Bitboard(self.bbs['P'].bb | self.bbs['N'].bb | self.bbs['B'].bb | self.bbs['R'].bb | self.bbs['Q'].bb | self.bbs['K'].bb)
  
  @property
  def black_pieces(self) -> Bitboard:
    return Bitboard(self.bbs['p'].bb | self.bbs['n'].bb | self.bbs['b'].bb | self.bbs['r'].bb | self.bbs['q'].bb | self.bbs['k'].bb)
  