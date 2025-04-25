
from mars.bitboard import Bitboard

# 1. Generate movement masks for rooks and bishops for each square on the board
# -  Relevant bits don't include the piece square or the board edges
# 2. For each mask, generate all possible "blocker" options
# 3. Use brute force to find a "magic" number that, when multiplied by the occupancy bitboard, produces a UNIQUE index
#    that can be used to generate a lookup table.
# 4. Use these lookup tables in rook and bishop move generation.
#    A Queen's moves are the intersection of the rook and bishop moves for a given origin square



