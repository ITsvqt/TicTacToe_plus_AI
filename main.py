
"""

# Tic-Tac-Toe v.1.0

"""
from engine.game import Game
from core.player.human_player import HumanPlayer
from core.player.ai1_random import AIRandom_Player
from core.player.ai2_wining_moves import AIWinningMoves_Player
from core.player.ai3_winning_and_loosing_moves import AIWinningAndLosingMoves_Player
from core.player.ai4_minmax import AIMinMax_Player




g1 = Game(
    (AIWinningAndLosingMoves_Player("P1", "X"),
     HumanPlayer("Gosheca", "O"))
    )

g1.game_loop()

    
print()