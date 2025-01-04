# Check for win conditions.

import sys
sys.path.append("./src")
from domain.board import Board
from game_exceptions import GameOverError
from services.score import ScoreService

class BoardStateService:
    def __init__(self, file_path:str):
        self.__score_serv = ScoreService(file_path)

    def record_state(self, board:Board, flag:bool):
        if len(board.free_cells) == 0:
            current_player = "You" if not flag else "The computer" 
            self.__score_serv.update_score(flag)
            raise GameOverError(current_player)
    
    @property
    def score_serv(self):
        return self.__score_serv