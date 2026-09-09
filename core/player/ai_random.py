
from core.player.base_player.player import Player
from core.player.mixin.ai_analysis import AIAnalysisMixin
import random

# class AIAnalysisMixin
class AIRandom_Player(Player, AIAnalysisMixin):
    
    
    def __init__(self, sign: str):
        super().__init__("Random Move", sign)
        
    def get_move(self, board_cells) -> tuple[int, int]:
        
        choice = random.choice(self._get_possible_moves(board_cells))
        return choice[1], choice[0]