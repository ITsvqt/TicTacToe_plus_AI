
from core.player.base_player.player import Player
from core.player.mixin.ai_analysis import AIAnalysisMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.board import Board

# class AIAnalysisMixin
class AIWinningMoves_Player(Player, AIAnalysisMixin):
    
    
    def __init__(self,name: str, sign: str):
        super().__init__(f"Wining Move AI - {name}", sign)
        
    def get_move(self, board: Board) -> tuple[int, int]:
        
        move = self.get_winning_move(board, self.sign)
        
        if move is not None:
            return move
        
        return self.get_random_move(board)
        
        

    

