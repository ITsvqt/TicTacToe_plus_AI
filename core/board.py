


class Board:
    """ Stores the current state of the board. """
    
    _CNT_SPACE_BETWEEN_CELLS = 1
    _CNT_SPACE_LEFT_PADDING = 2
    
    def __init__(self):
        
        self._size = 3
        self._data = [[" " for _ in range(self._size)] for _ in range(self._size)]
        
    @property
    def size(self):
        return self._size
    
    @property
    def data(self):
        return self._data
    
    def set_cell(self, x: int, y:int , symbol: str):
        " x axis maps to the second dimension, y to the first"
        self._data[y][x] = symbol
        
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
        for x in range(self._size):
            yield [self._data[y][x] for y in range(self._size)]
            
        # forward diagonal
        yield [self._data[i][i] for i in range(self._size)]
        
        # backward diagonal
        yield[self._data[i][-(i+1)] for i in range(self._size)]

            
    def map_line_and_index_to_coords(self, line_idx: int, el_idx: int) -> tuple[int, int]:
        """Map a line element index to board coordinates."""

        # if 0 <= line_idx <= 2:   # rows
        #     return el_idx, line_idx
        # elif 3 <= line_idx <= 5: # cols
        #     return line_idx - self._size, el_idx
        # elif line_idx == 6:      # forward diagonal
        #     return el_idx, el_idx
        # elif line_idx == 7:      # backward diagonal
        #     return  self._size - 1 - el_idx, el_idx
        
        if 0 <= line_idx <= 2:   # rows
            return line_idx, el_idx
        elif 3 <= line_idx <= 5: # cols
            return  el_idx, line_idx - self._size
        elif line_idx == 6:      # forward diagonal
            return el_idx, el_idx
        elif line_idx == 7:      # backward diagonal
            return  el_idx, self._size - 1 - el_idx 

    
        
    def render(self):
        print('\n'.join(self._get_render_lines()))
        
        
    def render_winning(self, line_index):
        #TODO: create robust rendering instead of changing what render returns
        #? board  row starts and index 2
        #? board  col starts and index 2 and have 1 element in between
        
        res = self._get_render_lines()
        
        if line_index <= 2:
            updated_line = res[line_index + 2]
            idx1 = self._CNT_SPACE_LEFT_PADDING
            idx2 = idx1 + 1 + self._CNT_SPACE_BETWEEN_CELLS
            idx3 = idx2 + 1 + self._CNT_SPACE_BETWEEN_CELLS
            updated_line = (
                f"{updated_line[0:idx1]}"
                f"\033[92m{updated_line[idx1]}\033[00m "
                f"\033[92m{updated_line[idx2]}\033[00m "
                f"\033[92m{updated_line[idx3]}\033[00m"
                f"{updated_line[idx3 + 1: ]}"
            )
            res[line_index + 2] = updated_line
            
        else:

            # get win coords
            win_cells_coords = set()
            for i in range(3):
                win_cells_coords.add(self.map_line_and_index_to_coords(line_index, i))
            
            # replace them in the original
            for win_cell_coords in win_cells_coords:
                x_wcc = win_cell_coords[0] + 2
                y_wcc = (win_cell_coords[1] * 2) + 2
                
                updated_line = res[x_wcc]
                update = f"\033[92m{updated_line[y_wcc]}\033[00m" # change to green color
                
                res[x_wcc] = updated_line[0:y_wcc] + update + updated_line[y_wcc + 1: ]
        
        print('\n'.join(res))
            
        
        
    def ensure_valid_position(self, x, y):
        """
            Error messages are in the 1 based index user format.
        """
        
        if (not 0 <= x <= self._size) or (not 0 <= y <= self._size):
            raise ValueError(f"[Move out of bound!] {x + 1}:{y + 1}")
        
        if self._data[y][x] != ' ':
            raise ValueError(f"[Move already played!] {x + 1}:{y + 1}")
        
        
    def _get_render_lines(self) -> list[str]:
        
        left_padding = " " * self._CNT_SPACE_LEFT_PADDING
        inbetween_padding = " " * self._CNT_SPACE_BETWEEN_CELLS
        
        result = []
        horizontal_frame = left_padding + '-' * 5
        
        result.append(left_padding + inbetween_padding.join([str(x) for x in range(1, self._size +1)]))
        result.append(horizontal_frame)
        for i in range(1, self._size + 1):
            result.append(f"{i}|" + inbetween_padding.join(self._data[i - 1]) + '|')
        result.append(horizontal_frame)
        
        return result
        
        
        
