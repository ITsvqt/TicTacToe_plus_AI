from typing import TYPE_CHECKING
import random

if TYPE_CHECKING:
    from core.board import Board

from engine.rules import TicTacToeRules

class AIAnalysisMixin:

    def get_random_move(self, board: Board):
        return random.choice(self.get_possible_moves(board))

    
    def get_winning_move(self, board: Board, player_sign: str) -> tuple[int,int] | None:
        """ Return None if no winning moves."""

        res = self._get_winning_line(board, player_sign)
    
        if res is not None:
            (x, y) =  board.map_line_and_index_to_coords(res[0], res[1].index(None))
            
            return (x, y)
        
        return None
    
    
    def get_loosing_move(self, board: Board, player_sign: str) -> tuple[int, int] | None:
        """ Returns None if no blocking wining move for the other player. """
    
        enemy_sign = TicTacToeRules.get_opponent_sign(player_sign)
        
        res = self._get_winning_line(board, enemy_sign)
        
        if res is not None:
            (x, y) =  board.map_line_and_index_to_coords(res[0], res[1].index(None))
            # the contract is the player provies x, y axis, which board returns flipped
            return (x, y)
        
        return None
        
        
    def get_possible_moves(self, board: Board) -> list[tuple[int, int]]:
        """
            Returns
                tuple: el[0] -> x on the visual game axis (left to right)
                       el[1] -> y on the visual game axis (up and down)
        """
        
        return [
            (x, y)
            for x in range(1, board.BOARD_WIDTH + 1)
            for y in range(1, board.BOARD_HEIGHT + 1)
            if board.get_cell(x, y) is None
        ]
        
        
    @staticmethod
    def _get_winning_line(board: Board, sign: str) -> tuple[int, list] | None:
        """ Returns index of the returned line from board and the line containing 2 signs and empty cell. """
        
        for (i, line) in enumerate(board.lines()):
            if line.count(sign) == 2 and None in line:
                return (i, line)
            
        return None
        
        
        
