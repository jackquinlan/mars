import numpy as np

VALID_COLORS=["w", "b"]
VALID_PIECES=["p", "n", "b", "r", "q", "k", # black pieces
              "P", "N", "B", "R", "Q", "K"] # white pieces
PROMO_PIECES=["N", "B", "R", "Q"]

A_FILE=np.uint64(0x0101010101010101)
B_FILE=np.uint64(0x0202020202020202)
G_FILE=np.uint64(0x4040404040404040)
H_FILE=np.uint64(0x8080808080808080)

RANK_1=np.uint64(0x00000000000000FF)
RANK_2=np.uint64(0x000000000000FF00)
RANK_4=np.uint64(0x00000000FF000000)
RANK_5=np.uint64(0x000000FF00000000)
RANK_7=np.uint64(0x00FF000000000000)
RANK_8=np.uint64(0xFF00000000000000)

DEFAULT_FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

SQUARES=[
    "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
    "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
    "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
    "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
    "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
    "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
    "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
    "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8",
]

