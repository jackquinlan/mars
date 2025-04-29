from mars.bitboard import Bitboard
from mars import VALID_PIECES


class Board:
    def __init__(self, fen: str): 
        self.bitboards = self._load_from_fen(fen)

    @property
    def to_fen(self):
        fen_rows = []
        for rank in range(7, -1, -1):
            row = ""
            cnt = 0
            for file in range(0, 8):
                square = (rank * 8) + file
                square_occupied = False
                for p, bb in self.bitboards.items():
                    if bb.get_bit(square): 
                        square_occupied = True
                        if cnt > 0:
                            row += f"{cnt}"
                        row += f"{p}"
                        cnt = 0
                        break
                if not square_occupied:
                    cnt += 1
            if cnt > 0:
                row += f"{cnt}"
            fen_rows.append(row)
        # Join ranks together
        return "/".join(fen_rows)

    def occupied(self):
        oc = Bitboard(0)
        for bb in self.bitboards:
            oc |= self.bitboards[bb]
        return oc 
    
    def occupied_by_color(self, color: str):
        assert color in ["w", "b"], "Invalid color"
        # White pieces are represented by uppercase characters
        pieces = ["P", "N", "B", "R", "Q", "K"] if color == "w" else \
                 ["p", "n", "b", "r", "q", "k"]
        oc = Bitboard(0)
        for bb in self.bitboards:
            if bb in pieces: 
                oc |= self.bitboards[bb]
        return oc

    def empty(self):
        return Bitboard(~self.occupied().board) & Bitboard(0xFFFFFFFFFFFFFFFF)
    
    def piece_bitboard(self, piece: str):
        assert piece in VALID_PIECES, "Invalid piece"
        return self.bitboards[piece]

    def _load_from_fen(self, board: str) -> dict[str, Bitboard]:
        # Example input: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
        bitboards = {
            p: Bitboard(0) for p in VALID_PIECES
        }
        idx = 56 # start index @ A8
        for rank in board.split("/"):
            for char in rank:
                if char.isdigit():
                    idx += int(char)
                else:
                    assert char in VALID_PIECES, "Invalid piece"
                    bitboards[char].set_bit(idx)
                    idx += 1
            idx -= 16 # reset index to next rank
        return bitboards
    
    def pprint(self):
        # Print a "pretty" version of the Board. Useful for debugging.
        board_str = ""
        for rank in range(7, -1, -1):
            row = f"{rank+1} "
            for file in range(0, 8):
                square = (rank * 8) + file
                square_occupied = None 
                for piece in VALID_PIECES:
                    if self.bitboards[piece].get_bit(square):
                        square_occupied = piece 
                        break
                row += f"{square_occupied} " if square_occupied else "* "
            board_str += row.rstrip() + "\n"
        board_str += "  A B C D E F G H"
        print(board_str)
    
