
from core.player.base_player.player import Player
from core.player.mixin.ai_analysis import AIAnalysisMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.board import Board

# class AIAnalysisMixin
class AIRandom_Player(Player, AIAnalysisMixin):
    

    def __init__(self, sign: str):
        super().__init__("Random Move", sign)
        
        
    def get_move(self, board: Board) -> tuple[int, int]:
        
        return self.get_random_move(board)