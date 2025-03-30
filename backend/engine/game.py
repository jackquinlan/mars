from engine.board import Board
from engine.move_generation import MoveGen


class Game:
  def __init__(self):
    self.board = Board()
    self.moves = MoveGen(board=self.board)
