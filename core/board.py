


class Board:
    """ Stores the current state of the board. """
    
    BOARD_HEIGHT = 3
    BOARD_WIDTH  = 3
    
    # rendering
    _CNT_SPACE_BETWEEN_CELLS = 1
    _CNT_SPACE_LEFT_PADDING = 2


    def __init__(self):
        self._data = [[None for _ in range(self.BOARD_WIDTH)] for _ in range(self.BOARD_HEIGHT)]

    
    def get_cell(self, x: int, y: int):
        """ Params:\n
                x: horizontal index, 1-based\n
                y: vertical   index, 1-based
        """
        
        return self._data[y - 1][x - 1]
    
    
    def set_cell(self, x: int, y:int , symbol: str):
        """ Params:\n
                x: horizontal index, 1-based\n
                y: vertical   index, 1-based
        """
        
        self._data[y - 1][x - 1] = symbol
        
        
    def lines(self):
        """ 
            Yield each row, column, and diagonal of the board.

            Yields:
                list[str]: The cells making up one line of the board.
        """
          
        # horizontal
        for row in self._data:
            yield row
            
        # vertical
        for x in range(self.BOARD_HEIGHT):
            yield [self._data[y][x] for y in range(self.BOARD_WIDTH)]
            
        # forward diagonal
        yield [self._data[i][i] for i in range(self.BOARD_HEIGHT)]
        
        # backward diagonal
        yield[self._data[i][-(i+1)] for i in range(self.BOARD_HEIGHT)]

            
    def map_line_and_index_to_coords(self, line_idx: int, el_idx: int) -> tuple[int, int]:
        """ Params\n
            line_idx: index of line returned from Board.lines\n
            el_idx  : index of element in that line\n
            Returns\n
            tuple[0] horizontal index, 1-based\n
            tuple[1] vertical index, 1-based
        """

        if 0 <= line_idx <= 2:   # rows
            return el_idx + 1, line_idx + 1
        elif 3 <= line_idx <= 5: # cols
            return  (line_idx - self.BOARD_HEIGHT) + 1, el_idx + 1
        elif line_idx == 6:      # forward diagonal
            return el_idx + 1, el_idx + 1
        elif line_idx == 7:      # backward diagonal
            return  self.BOARD_HEIGHT - el_idx, el_idx + 1

    
    
    def ensure_valid_position(self, x, y):
        """
            x: horizontal coord, 1-based
            y: vertical coord, 1-based
        """
        
        if (not 1 <= x <= self.BOARD_WIDTH) or (not 1 <= y <= self.BOARD_HEIGHT):
            raise ValueError(f"[Move out of bound!] {x}:{y}")
        
        
    def render(self, winning_line_idx = None):
        
        left_padding = " " * self._CNT_SPACE_LEFT_PADDING
        inbetween_padding = " " * self._CNT_SPACE_BETWEEN_CELLS
        
        result = []
        horizontal_frame = left_padding + '-' * 5
        
        # constant
        result.append(left_padding + inbetween_padding.join([str(x) for x in range(1, self.BOARD_WIDTH + 1)]))
        result.append(horizontal_frame)
        
        
        # variable / robust
        # Using boards interface for matrix coordinates,
        # to reuse public functions,
        # without adding new stuff
        if winning_line_idx is None:
            for y in range(1, self.BOARD_HEIGHT + 1):
                row = [self._get_render_cell(x, y) for x in range(1, self.BOARD_WIDTH + 1)]
                result.append(f"{y}|" + inbetween_padding.join(row) + '|')
        else:
            
            winning_coords = {
                self.map_line_and_index_to_coords(winning_line_idx, i)
                for i in range(self.BOARD_HEIGHT)
            }
            for y in range(1, self.BOARD_HEIGHT + 1):
                row = [self._get_render_cell(x, y, winning_coords) for x in range(1, self.BOARD_WIDTH + 1)]
                result.append(f"{y}|" + inbetween_padding.join(row) + '|')
 
 
        # constant
        result.append(horizontal_frame)
        
        
        print('\n'.join(result))
        
    def _get_render_cell(self, x, y, winning_coords = None):
        
        cell = self.get_cell(x, y)
        
        if cell is None:
            return " "
        
        if winning_coords and (x, y) in winning_coords:
            return f"\033[92m{cell}\033[00m"
        
        return cell


    # def render_winning(self, line_index):
    #         #TODO: create robust rendering instead of changing what render lines returns
    #         #? board  row starts and index 2
    #         #? board  col starts and index 2 and have 1 element in between
            
    #         res = self._get_render_lines()
            
    #         if line_index <= 2:
    #             updated_line = res[line_index + 2]
    #             idx1 = self._CNT_SPACE_LEFT_PADDING
    #             idx2 = idx1 + 1 + self._CNT_SPACE_BETWEEN_CELLS
    #             idx3 = idx2 + 1 + self._CNT_SPACE_BETWEEN_CELLS
    #             updated_line = (
    #                 f"{updated_line[0:idx1]}"
    #                 f"\033[92m{updated_line[idx1]}\033[00m "
    #                 f"\033[92m{updated_line[idx2]}\033[00m "
    #                 f"\033[92m{updated_line[idx3]}\033[00m"
    #                 f"{updated_line[idx3 + 1: ]}"
    #             )
    #             res[line_index + 2] = updated_line
                
    #         else:

    #             # get win coords
    #             win_cells_coords = set()
    #             for i in range(3):
    #                 win_cells_coords.add(self.map_line_and_index_to_coords(line_index, i))
                
    #             # replace them in the original
    #             for win_cell_coords in win_cells_coords:
    #                 x_wcc = win_cell_coords[0] + 2
    #                 y_wcc = (win_cell_coords[1] * 2) + 2
                    
    #                 updated_line = res[x_wcc]
    #                 update = f"\033[92m{updated_line[y_wcc]}\033[00m" # change to green color
                    
    #                 res[x_wcc] = updated_line[0:y_wcc] + update + updated_line[y_wcc + 1: ]
            
    #         print('\n'.join(res))
            

        
        
        
