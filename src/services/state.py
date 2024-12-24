# Check for win conditions.

import sys
sys.path.append("./src")
from domain.board import Board
from game_exceptions import GameOverError
from repository.score_repo import ScoreRepo

class BoardStateService:
    def __init__(self):
        self.__score_repo = ScoreRepo("src/repository/score.txt")

    def record_state(self, board:Board, flag:bool):
        if BoardStateService.check_game_over(board) == True:
            current_player = "You" if not flag else "The computer" 
            self.__score_repo.update_score(flag)
            raise GameOverError(current_player)

    @staticmethod
    def check_game_over(board:Board):
        for i in range(0, 6):
            for j in range(0, 6):
                if board[i, j] == ' ':
                    return False
        
        return True