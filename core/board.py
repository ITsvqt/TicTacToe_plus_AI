


class Board:
    """ Stores the current state of the board. """
    
    
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

        
    def render(self):
        
        result = []
        horizontal_frame = '  ' + '-' * 5
        
        result.append("  " + " ".join([str(x) for x in range(1, self._size +1)]))
        result.append(horizontal_frame)
        for i in range(1, self._size + 1):
            result.append(f"{i}|" + " ".join(self._data[i - 1]) + '|')
        result.append(horizontal_frame)
        
        print('\n'.join(result))
        
        
    def ensure_valid_position(self, x, y):
        """
            Error messages are in the 1 based index user format.
        """
        
        if (not 0 <= x <= self._size) or (not 0 <= y <= self._size):
            raise ValueError(f"[Move out of bound!] {x + 1}:{y + 1}")
        
        if self._data[y][x] != ' ':
            raise ValueError(f"[Move already played!] {x + 1}:{y + 1}")
        
        
