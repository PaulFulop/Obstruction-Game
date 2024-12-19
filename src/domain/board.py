#Board for the game (texttable object)

from texttable import Texttable

class Board(Texttable):
    def __init__(self):
        self.__board = Texttable()
        rows = [[' ' for _ in range(6)] for _ in range(6)]
        self.__board.add_rows(rows, header=False)
    
    def __str__(self):
        return self.__board.draw()

    def __getitem__(self, index):
        pass

    def __setitem__(self, index):
        pass
    
    def get_rows(self):
        return self.__board._rows

    def place_X(self):
        pass


board = Board()