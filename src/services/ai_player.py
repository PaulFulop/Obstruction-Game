#Service for the computer moves. How should the AI play (minmax alg.)

import sys
sys.path.append("./src")
from domain.board import Board
from services.moves import MoveService

class AIPlayerService:
    def __init__(self, moves_service:MoveService, symbol:str):
        self.__moves_service = moves_service
        self.__symbol = symbol

    def make_move(self):
        best_score = -100000 if self.__symbol == 'O' else 100000
        best_move = None
        is_maximizing = (self.__symbol == 'O') # True if we are the max player, False otherwise

        for x, y in self.__moves_service.board.free_cells:
            self.__moves_service.mark(x, y, self.__symbol)
            score = self.minimax(not is_maximizing, 0)
            self.__moves_service.undo()

            if (is_maximizing and score > best_score) or (not is_maximizing and score < best_score):
                best_score = score
                best_move = (x, y)
        
        self.__moves_service.mark(best_move[0], best_move[1], self.__symbol)

    def minimax(self, max_player:bool, depth:int):
        if self.__terminal_state() == True:
            return self.__eval_function(max_player)
        
        if max_player == True:
            best = -1001
            for move in self.__moves_service.board.free_cells:
                self.__moves_service.mark(move[0], move[1], 'O')
                best = max(best, self.minimax(False, depth + 1) + (36 - len(self.__moves_service.board.free_cells)))
                self.__moves_service.undo() 
            #print(depth)
            return best
        else:
            best = 1001
            for move in self.__moves_service.board.free_cells:
                self.__moves_service.mark(move[0], move[1], 'X')
                best = min(best, self.minimax(True, depth + 1) - (36 - len(self.__moves_service.board.free_cells)))
                self.__moves_service.undo()
            #print(depth)
            return best


    def __terminal_state(self):
        return len(self.__moves_service.board.free_cells) == 0

    # returns 1 if on a state of the board the first player wins, -1 otherwise
    def __eval_function(self, max_player:bool):
        return 1000 if not max_player == True else -1000


# board = Board()
# move = MoveService(board)
# move.mark(0, 0, 'X')
# move.mark(0, 2, 'X')
# move.mark(0, 4, 'X')

# move.mark(5, 5, 'X')
# move.mark(2, 2, 'X')
# move.mark(2, 4, 'X')
# move.mark(5, 1, 'X')

#move.mark(4, 0, 'X')
# move.mark(4, 2, 'X')
# move.mark(4, 4, 'X')

#print(len(move.board.free_cells))

# ai1 = AIPlayerService(move, 'O')
# ai2 = AIPlayerService(move, 'X')

# ai1.make_move()
# print(board)

#try:
    #ai1.make_move()
    #ai2.make_move()
    # ai1.make_move()
    # ai2.make_move()
    # ai1.make_move()
#except Exception as e:
    #print(e)