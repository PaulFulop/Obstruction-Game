#Service for the computer moves. How should the AI play (minmax alg.)

import sys
sys.path.append("./src")
from domain.board import Board
from services.moves import MoveService

class AIPlayerService:
    def __init__(self, moves_service:MoveService, symbol:str):
        self.__moves_service = moves_service
        self.__symbol = symbol
    
    # minimax alg functions below
    def make_move(self):
        pass

    def minimax(self):
        pass