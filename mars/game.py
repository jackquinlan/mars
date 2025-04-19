from mars.movegen  import MoveGen
from mars.position import Position
from mars import DEFAULT_FEN


class Game:
    def __init__(self, initial_fen: str=DEFAULT_FEN):
        self.position = Position.load_from_fen(fen=initial_fen)
        self.move_gen = MoveGen()

    def loop(self):
        moves = self.move_gen.pseudo_legal_moves(position=self.position)
        for move in moves:
            print(move)
        return

