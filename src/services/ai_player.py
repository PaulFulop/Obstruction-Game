#Service for the computer moves. How should the AI play (minmax alg.)

import sys, random
sys.path.append("./src")
from domain.board import Board
from services.moves import MoveService
from services.state import BoardStateService

class AIPlayerService:
    def __init__(self, moves_service:MoveService, symbol:str):
        self.__moves_service = moves_service
        self.__symbol = symbol
    
    # minimax alg functions below
    def make_move(self):
        x = random.randint(0, 5)
        y = random.randint(0, 5)

        while(self.__moves_service.board[x, y] != ' '):
            x = random.randint(0, 5)
            y = random.randint(0, 5)
        
        self.__moves_service.mark(x, y, self.__symbol, 0)

    def minimax(self):
        pass


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