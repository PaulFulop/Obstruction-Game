# Allowing players to make moves (marking an X or O on the board)

import sys
sys.path.append("./src")
from domain.board import Board
from game_exceptions import OutOfBoardError, OccpiedCellError

class MoveService:
    __directions = [(0, 0), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1), (1, -1)]


    def __init__(self, board:Board):
        self.__board = board
        self.__history = []
    
    def cells_to_mark(self, x:int, y:int, k:int, cells:list):
        if k > 8:
            self.__history.append(cells[:])
            return

        if x + MoveService.__directions[k][0] < 0 or x + MoveService.__directions[k][0] > 5 or y + MoveService.__directions[k][1] < 0 or y + MoveService.__directions[k][1] > 5:
            if k:
                self.cells_to_mark(x, y, k + 1, cells)
                return

            raise OutOfBoardError

        if (x + MoveService.__directions[k][0], y + MoveService.__directions[k][1]) not in self.__board.free_cells:
            if k:
                self.cells_to_mark(x, y, k + 1, cells)
                return
            
            raise OccpiedCellError(x, y)

        self.cells_to_mark(x, y, k + 1, cells + [(x + MoveService.__directions[k][0], y + MoveService.__directions[k][1])])

    def mark(self, x:int, y:int, symbol:str):
        self.cells_to_mark(x, y, 0, [])
        row, col = self.__history[-1][0]
        self.__board[row, col] = symbol

        for row, col in self.__history[-1][1:]:
            self.__board[row, col] = '*'
    
    def undo(self):
        if len(self.__history) > 0:
            for row, col in self.__history[-1]:
                self.__board[row, col] = ' '

            self.__history.pop()

    @property
    def board(self):
        return self.__board

    @property
    def history(self):
        return self.__history

board = Board()
move = MoveService(board)