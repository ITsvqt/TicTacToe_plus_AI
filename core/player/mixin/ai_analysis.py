from typing import TYPE_CHECKING
import random

if TYPE_CHECKING:
    from core.board import Board


class AIAnalysisMixin:

    def get_random_move(self, board: Board):
        choice = random.choice(self._get_possible_moves(board))
        return choice[1], choice[0]
    
    
    
    def get_winning_move(self, board: Board, player_sign: str) -> tuple[int,int] | None:
        """ Return None if no winning moves."""

        res = self._get_winning_line(board, player_sign)
    
        if res is not None:
            y, x =  board.map_line_and_index_to_coords(res[0], res[1].index(' '))
            # the contract is the player provies x, y axis, which board returns flipped
            return x,y
        
        return None
    
    
    def get_loosing_move(self, board: Board, player_sign: str) -> tuple[int, int] | None:
        """ Returns None if no blocking wining move for the other player. """
    
        enemy_sign = 'X' if player_sign == 'O' else 'O'
        
        res = self._get_winning_line(board, enemy_sign)
        
        if res is not None:
            y, x =  board.map_line_and_index_to_coords(res[0], res[1].index(' '))
            # the contract is the player provies x, y axis, which board returns flipped
            return x,y
        
        return None
        
        
    @staticmethod
    def _get_possible_moves(board: Board) -> list[tuple[int, int]]:
        return [
            (x, y)
            for y in range(board.size)
            for x in range(board.size)
            if board.data[x][y] == " "
        ]
        
        
    @staticmethod
    def _get_winning_line(board: Board, sign: str) -> tuple[int, list] | None:
        """ Returns index of the returned line from board and the line containing 2 signs and empty cell. """
        
        for i, line in enumerate(board.lines()):
            if line.count(sign) == 2 and ' ' in line:
                return i, line
            
        return None
        
        
    # @staticmethod
    # def _map_line_and_index_to_cords(line_idx: int, el_idx: int, board_size: int) -> tuple[int, int]:
    #     """ Maps index of element in the returned board.lines to board.matrix coordinate. """

    #     if 0 <= line_idx <= 2:
    #         return el_idx, line_idx
    #     elif 3 <= line_idx <= 5:
    #         return line_idx - board_size, el_idx
    #     elif line_idx == 6:
    #         return el_idx, el_idx
    #     elif line_idx == 7:
    #         return  board_size - 1 - el_idx, el_idx
    
        
        
