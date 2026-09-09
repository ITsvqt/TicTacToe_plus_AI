
import os

from core.board import Board
from core.player.base_player.player import Player

class Game:
    
    def __init__(self, players: tuple[Player, Player]):
        
        self._ensure_valid_player_cnt(players)
        
        self._board = Board()
        self._players: tuple[Player, Player] = players
        
        self._current_player = 0
        
        self._cnt_max_moves = self._board.size * self._board.size
        self._cnt_moves = 0
        
        
    def game_loop(self):
    
        while True:
            
            self._clear_and_print_board()
 
            player = self._players[self._current_player]
            move = self._get_valid_move(player)
            
            self._board.set_cell(*move, player.sign)
            
            #TODO: print the board highliting the winner line in green + cool message
            if self._is_winner(player):
                self._clear_and_print_board()
                print(f"Player \'{player.name}\' WON !!")
                break
            
            self._cnt_moves += 1
            
            #TODO: highlight everyting in orange + cool message
            if self._is_draw():
                self._clear_and_print_board()
                print("Game ended in a DRAW !!")      
                break
                
            # set current player id
            self._current_player = (self._current_player + 1) % len(self._players)



    def _get_valid_move(self, player: Player):
                
        while True:
            
            try:
                move = player.get_move(self._board)
                self._board.ensure_valid_position(*move)
                return move
            
            except ValueError as error:
                print(error)
                input("Press Enter to Continue ...")
                self._clear_and_print_board()
                
    
    def _is_winner(self, player: Player):
        
        for line in self._board.lines():
            if line.count(player.sign) == 3:
                return True
            
        return False
    
    
    def _is_draw(self):
        if self._cnt_max_moves == self._cnt_moves:
            return True
        
        return False
        

    @staticmethod
    def _ensure_valid_player_cnt( players):
        if len(players) != 2:
            raise ValueError("Game craetion: expects exactly 2 players!")


    @staticmethod
    def _clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
    def _clear_and_print_board(self):
        self._clear_screen()
        self._board.render()
        
