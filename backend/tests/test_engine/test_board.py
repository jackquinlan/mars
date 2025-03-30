import unittest

from engine.bitboards import Bitboard
from engine.game import Game

class TestBoard(unittest.TestCase):

  def test_initialization(self):
    game = Game()
    game.moves.double_push_pawn_targets()
