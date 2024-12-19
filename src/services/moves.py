# Allowing players to make moves (marking an X or O on the board).
# Validating moves (ensuring the chosen cell is empty and within bounds).
# Drawing the contour around X/0 

import sys
sys.path.append("./src")
from domain.board import Board
from services.state import BoardStateService


# TODO make custom exceptions
class MoveService:
    __directions = [(0, 0), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1), (1, -1)]


    def __init__(self, board:Board, flag:bool):
        self.__board = board
        self.__flag = flag
        self.__board_state = BoardStateService()

    def mark(self, x:int, y:int, symbol:str, k:int):
        if k > 8:
            return
        if x + MoveService.__directions[k][0] < 0 or x + MoveService.__directions[k][0] > 5 or y + MoveService.__directions[k][1] < 0 or y + MoveService.__directions[k][1] > 5:
            if symbol == '*':
                self.mark(x, y, '*', k + 1)
                return

            raise ValueError("Out of bounds.")

        if self.__board[x, y] != ' ' and symbol != '*':
            raise ValueError("Can't put it there.")
        
        self.__board_state.record_state(self.__board, self.__flag)
        self.__board[x + MoveService.__directions[k][0], y + MoveService.__directions[k][1]] = symbol
        self.mark(x, y, '*', k + 1)
        self.__flag = not self.__flag
    
    @property
    def flag(self):
        return self.__flag

board = Board()
move = MoveService(board, 0)
move.mark(0, 0, 'X', 0)
move.mark(1, 2, 'O', 0)
move.mark(2, 0, 'X', 0)
print(board)