

class AIAnalysisMixin:
    
    @staticmethod
    def _get_possible_moves(board_cells) -> list[tuple[int, int]]:
        return [
            (x, y)
            for y in range(len(board_cells))
            for x in range(len(board_cells[y]))
            if board_cells[x][y] == " "
        ]
