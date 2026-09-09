
from core.player.base_player.player import Player

class HumanPlayer(Player):
    
    def __init__(self, name: str, sign: str):
        super().__init__(name, sign)

    def get_move(self, _) -> tuple[int, int]:
        
        print(f"Player {self._name} with {self._sign} sign")
        x = input("  Enter X cordinate \u2192 : ")
        y = input("  Enter Y cordinate \u2193 : ")
        
        try:
            x,y = map(int, (x,y))
        except:
            raise ValueError("[Invalid cordinate type!] Number expected.")
        
        return (x - 1, y - 1)