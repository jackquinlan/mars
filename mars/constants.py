import numpy as np

VALID_COLORS=["w", "b"]
VALID_PIECES=["p", "n", "b", "r", "q", "k", # black pieces
              "P", "N", "B", "R", "Q", "K"] # white pieces
PROMO_PIECES=["N", "B", "R", "Q"]

A_FILE=np.uint64(0x0101010101010101)
H_FILE=np.uint64(0x8080808080808080)

RANK_1=np.uint64(0x00000000000000FF)
RANK_2=np.uint64(0x000000000000FF00)
RANK_4=np.uint64(0x00000000FF000000)
RANK_5=np.uint64(0x000000FF00000000)
RANK_7=np.uint64(0x00FF000000000000)
RANK_8=np.uint64(0xFF00000000000000)

DEFAULT_FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

SQUARES=[
    "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
    "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8",
    "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", 
    "D1", "C2", "D3", "D4", "D5", "D6", "D7", "D8",
    "E1", "D2", "E3", "E4", "E5", "E6", "E7", "E8",
    "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8",
    "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8",
    "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8",
]

