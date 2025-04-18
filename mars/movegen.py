from dataclasses import dataclass
from typing import Optional
from mars.position import Position


@dataclass(frozen=True)
class Move:
    start: int 
    end: int   
    position: Optional[str] = None # Q, R, B, or N
    
class MoveGen:
    def __init__(self):
        return
    
    def pseudo_legal_moves(self, position: Position) -> list[Move]:
        return []
    
    def pawn_moves(self):
        return

