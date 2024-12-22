#Human player service (how should the human move)

import sys
sys.path.append("./src")
from domain.board import Board
from services.moves import MoveService
from services.state import BoardStateService

class HumanPlayerService:
    def __init__(self, moves_service:MoveService, symbol:str, ):
        self.__moves_service = moves_service
        self.__symbol = symbol
        self.__board_state = BoardStateService
    
    def make_move(self, x:int, y:int):
        self.__board_state.record_state(self.__moves_service.board, 1)
        self.__moves_service.mark(x, y, self.__symbol)