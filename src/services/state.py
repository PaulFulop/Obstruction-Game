# Check for win conditions.

import sys
sys.path.append("./src")
from domain.board import Board

# TODO  have custom exceptions
class BoardStateService:
    @staticmethod
    def record_state(board:Board, flag:bool):
        if BoardStateService.check_game_over(board) == True:
            current_player = "You" if not flag else "The computer" 
            raise ValueError(f"{current_player} won!")

    @staticmethod
    def check_game_over(board:Board):
        for i in range(0, 6):
            for j in range(0, 6):
                if board[i, j] == ' ':
                    return False
        
        return True