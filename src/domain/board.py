#Board for the game

from texttable import Texttable
from rich.console import Console
from rich.text import Text

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
    def __init__(self):
        self.__board = CustomTextTable()
        rows = [[' ' for _ in range(6)] for _ in range(6)]
        self.__board.add_rows(rows, header=False)
    
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

# board = Board()
# board[1, 2] = 'O'
# board[1, 3] = 'X'
# board[2, 3] = '*'
# print(board)