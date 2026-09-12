
from core.player.base_player.player import Player
from core.player.mixin.ai_analysis import AIAnalysisMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.board import Board
    
import copy
    

# class AIAnalysisMixin
class AIMinMax_Player(Player, AIAnalysisMixin):
    
    
    def __init__(self, name: str,  sign: str):
        super().__init__(f"MinMax AI - {name}", sign)
        
    def get_move(self, board: Board) -> tuple[int, int]:
        self._minmax_move(board, "X")
    

    # def _minmax_move(self, board: Board, who_am_i):
        
    #     best_move = None
    #     best_score = None

    #     for move in self.get_possible_moves(board):
    #         _board = copy.deepcopy(board.data)
    #         _board[move[1]][move[0]] = self.sign

    #         opp = "X" if self.sign == "O" else "O"
            
    #         score = self._minmax_score(_board, opp, self.sign)
    #         if best_score is None or score > best_score:
    #             best_move = move
    #             best_score = score

    #     return best_move


    # def _minmax_score(self, board, player_to_move, player_to_optimize):
        
    #     winner = ttt.get_winner(board)
        
    #     if winner is not None:
    #         if winner == player_to_optimize:
    #             return 10
    #         else:
    #             return -10
    #     elif ttt.is_board_full(board):
    #         return 0

    #     legal_moves = utils.get_all_legal_moves(board)

    #     scores = []
    #     for move in legal_moves:
    #         _board = copy.deepcopy(board)
    #         _board[move[1]][move[0]] = player_to_move


    #         opp = "X" if player_to_move == "O" else "O"

    #         opp_best_response_score = self._minmax_score(_board, opp, player_to_optimize)
    #         scores.append(opp_best_response_score)

    #     if player_to_move == player_to_optimize:
    #         return max(scores)
    #     else:
    #         return min(scores)
        
        
    # def _get_winner
        
        