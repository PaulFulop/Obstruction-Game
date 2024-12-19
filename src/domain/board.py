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
            
            self._rows[row][column] = value
        else:
            raise IndexError("Invalid index format.")

class Board:
    def __init__(self):
        self.__board = CustomTextTable()
        rows = [[' ' for _ in range(6)] for _ in range(6)]
        self.__board.add_rows(rows, header=False)
    
    def __str__(self):
        return self.__board.draw()
    
    def __getitem__(self, index):
        return self.__board.__getitem__(index)
    
    def __setitem__(self, index, value):
        self.__board.__setitem__(index, value)

# board = Board()
# board[2, 3] = '2'
# print(board)