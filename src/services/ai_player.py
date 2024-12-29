#Service for the computer moves. How should the AI play (minmax alg.)

import sys
sys.path.append("./src")
from domain.board import Board
from services.moves import MoveService

class AIPlayerService:
    def __init__(self, moves_service:MoveService, symbol:str):
        self.__moves_service = moves_service
        self.__symbol = symbol

    def make_move(self):
        pass

    def minimax(self, board:Board, max_player:bool):
        if self.__terminal_state():
            return self.__eval_function(max_player)
        
        if max_player == True:
            for move in self.__moves_service.board.free_cells:
                pass

    def __terminal_state(self):
        return len(self.__moves_service.board.free_cells) == 0

    # returns 1 if on a state of the board the first player wins, -1 otherwise
    def __eval_function(self, max_player:bool):
        return 1000 if max_player == True else -1000


# board = Board()
# move = MoveService(board)
# ai = AIPlayerService(move, '0')
# try:
#     ai.make_move()
#     ai.make_move()
#     ai.make_move()
#     ai.make_move()
#     ai.make_move()
# except Exception as e:
#     print(e)
# print(board)