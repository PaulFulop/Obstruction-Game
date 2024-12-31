# Class that encapsulated all the other services.

import sys
sys.path.append("./src")
from domain.board import Board
from services.ai_player import AIPlayerService
from services.human_player import HumanPlayerService
from services.moves import MoveService
from services.state import BoardStateService

from enum import Enum
class Players(Enum):
    HUMAN_PLAYER = 0
    AI_PLAYER = 1

class GameInit:
    def __init__(self, firstPlayer:Players, difficulty:int):
        self.__board = Board()
        self.__moves_service = MoveService(self.__board)
        self.__state = BoardStateService()

        if firstPlayer.name == "HUMAN_PLAYER":
            self.__flag = False
            self.__human = HumanPlayerService(self.__moves_service, "O")
            self.__computer = AIPlayerService(self.__moves_service, "X", difficulty)
        else:
            self.__flag = True
            self.__human = HumanPlayerService(self.__moves_service, "X")
            self.__computer = AIPlayerService(self.__moves_service, "O", difficulty)
    
    def clear_board(self):
        for i in range(0, 6):
            for j in range(0, 6):
                self.__board[i, j] = ' '

    @property
    def board(self):
        return self.__board
    
    @property
    def flag(self):
        return self.__flag
    
    @property
    def human(self):
        return self.__human
    
    @property
    def computer(self):
        return self.__computer
    
    @property
    def state(self):
        return self.__state