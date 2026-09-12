
from core.board import Board


class TicTacToeRules:
    
    @staticmethod
    def get_winner(board: Board) -> tuple[int, str] | None:
        """ Returns idx of the line from Board.lines() and player sign ('X' or 'O'). """
        for i, line in enumerate(board.lines()):
            if len(set(line)) == 1 and line[0] is not None:
                return (i, line[0])
        
        return None
    
    
    @staticmethod
    def is_board_full(board_size: int, move_count) -> bool:
        return board_size == move_count
    
    
    @staticmethod
    def ensure_valid_move(board: Board, x: int, y: int):
        
        board.ensure_valid_position(x, y)
        
        if board.get_cell(x, y) is not None:
            raise ValueError(f"[Move already played!] {x}:{y}")
        
    @staticmethod
    def get_opponent_sign(sign: str) -> str:
        
        if sign == "X":
            return "O"
        
        if sign == "O":
            return "X"
        
        raise ValueError(f"Invalid player sign: {sign}")
