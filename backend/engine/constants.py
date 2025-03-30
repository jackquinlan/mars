# LERF mapping constants
FILE_A = 0x0101010101010101
FILE_H = 0x8080808080808080
RANK_1 = 0x00000000000000FF
RANK_4 = 0x00000000FF000000
RANK_5 = 0x000000FF00000000
RANK_8 = 0xFF00000000000000

# Used to avoid wrapping around the board
NOT_A_FILE = ~FILE_A
NOT_H_FILE = ~FILE_H

WHITE_SQUARES = 0x55AA55AA55AA55AA
BLACK_SQUARES = 0xAA55AA55AA55AA55

# uppercase = white pieces, lowercase = black pieces
PIECES = ['P', 'N', 'B', 'R', 'Q', 'K', 'p', 'n', 'b', 'r', 'q', 'k']