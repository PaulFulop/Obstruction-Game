#Human player service (how should the human move)

import sys
sys.path.append("./src")
from services.moves import MoveService

class HumanPlayerService:
    def __init__(self, moves_service:MoveService, symbol:str):
        self.__moves_service = moves_service
        self.__symbol = symbol
    
    def make_move(self, x:int, y:int):
        self.__moves_service.mark(x, y, self.__symbol)