# Basically the main service which handles the whole functionality and logic of the game using the other services.

import sys
sys.path.append("./src")
from domain.board import Board
from services.ai_player import AIPlayerService
from services.human_player import HumanPlayerService
from services.moves import MoveService
from enum import Enum
class Players(Enum):
    HUMAN_PLAYER = 0
    AI_PLAYER = 1

class GameService:
    def __init__(self, firstPlayer:Players):
        self.__board = Board()
        self.__moves_service = MoveService(self.__board)

        if firstPlayer.name == "HUMAN_PLAYER":
            self.__flag = False
            self.__human = HumanPlayerService(self.__moves_service, "0")
            self.__computer = AIPlayerService(self.__moves_service, self.__board, "X")
        else:
            self.__flag = True
            self.__human = HumanPlayerService(self.__moves_service, "X")
            self.__computer = AIPlayerService(self.__moves_service, self.__board, "0")
    
    def play_turn(self, x:int, y:int):
        if self.__flag == False:
            self.__human.make_move(x, y)
            self.__computer.make_move()
        else:
            self.__computer.make_move()
            self.__human.make_move(x, y)

    @property
    def board(self):
        return self.__board