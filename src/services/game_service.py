# Basically the main service which handles the whole functionality and logic of the game using the other services.

import sys
sys.path.append("./src")
from domain.board import Board
from services.ai_player import AIPlayerService
from services.human_player import HumanPlayerService
from services.moves import MoveService
from start import Players

class GameService:
    def __init__(self, firstPlayer:Players):
        self.__board = Board()
        self.__human = HumanPlayerService()
        self.__computer = AIPlayerService()

        if firstPlayer.name == "HUMAN_PLAYER":
            self.__flag = False
        else:
            self.__flag = True
    
    def run_game(self):
        pass