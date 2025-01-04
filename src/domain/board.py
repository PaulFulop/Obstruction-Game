#Board for the game

from texttable import Texttable

class CustomTextTable(Texttable):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return self.draw()

    def __getitem__(self, index):
        if isinstance(index, tuple) and len(index) == 2:
            row, column = index
            if row < 0 or row > 5:
                raise IndexError("Row index out of range.")

            if column < 0 or column > 5:
                raise IndexError("Column index out of range.")
            
            return self._rows[row][column]
        else:
            raise IndexError("Invalid index format.")

    def __setitem__(self, index, value):
        if isinstance(index, tuple) and len(index) == 2:
            row, column = index
            if row < 0 or row > 5:
                raise IndexError("Row index out of range.")

            if column < 0 or column > 5:
                raise IndexError("Column index out of range.")
            
            self._rows[row][column] = str(value)
        else:
            raise IndexError("Invalid index format.")

class Board:

    BORDER_COLOR = (32, 34, 36)
    LIGHT_GREY = (212, 210, 217)
    BLUE = (60, 133, 181)
    RED = (186, 17, 17)

    def __init__(self):
        self.__board = CustomTextTable()
        rows = [[' ' for _ in range(6)] for _ in range(6)]
        self.__board.add_rows(rows, header=False)
        self.__free_cells = [(i, j) for i in range(6) for j in range(6)] 
    
    def __str__(self):
        brown = f"\x1b[38;2;{99};{70};{43}m"
        blue = f"\x1b[38;2;{60};{133};{181}m"
        red = f"\x1b[38;2;{186};{17};{17}m"
        grey = f"\x1b[38;2;{212};{210};{217}m"
        reset_color = "\x1b[0m"
        raw_board = self.__board.draw().replace('+', f"{brown}+{reset_color}").replace('-', f"{brown}-{reset_color}").replace('|', f"{brown}|{reset_color}")
        return raw_board.replace('X', f"{blue}X{reset_color}").replace('O', f"{red}O{reset_color}").replace('*', f"{grey}*{reset_color}")
    
    def __getitem__(self, index):
        return self.__board.__getitem__(index)
    
    def __setitem__(self, index, value):
        self.__board.__setitem__(index, value)

        if value == ' ' and index not in self.__free_cells:
            self.__free_cells.append(index)
        elif value != ' ' and index in self.__free_cells:
            self.__free_cells.remove(index)
    
    # Only works well for the empty board -> used for optimization on the minimax algorithm by reducing the number of moves to verify
    def filter_symmetric_positions(self):
        positions = self.free_cells[:]

        for position in positions:
            x, y = position
            
            if (y, 5 - x) in positions:
                positions.remove((y, 5 - x))

            if (5 - x, 5 - y) in positions:
                positions.remove((5 - x, 5 - y))
            
            if (5 - y, x) in positions:
                positions.remove((5 - y, x))
        
        return positions
    
    @property
    def free_cells(self):
        return self.__free_cells