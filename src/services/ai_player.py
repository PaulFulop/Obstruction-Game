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

    def minimax(self, board:Board, depth:int, max_player:bool):
        pass

    def __terminal_state(self):
        return len(self.__moves_service.board.free_cells) == 0

    # basically the score. the max player (X) wants to maximize this score and the min player (O) wants to minimize it
    def __value(self):
        value = self.__moves_service.board.free_cells
        return value if self.__symbol == 'X' else -value


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