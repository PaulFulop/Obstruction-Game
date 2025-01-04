#Service for the computer moves (how should the AI play)

import sys, random
sys.path.append("./src")
from domain.board import Board
from services.moves import MoveService

class AIPlayerService:
    def __init__(self, moves_service:MoveService, symbol:str, difficulty:int):
        match difficulty:
            case 1:
                self.__ai = StupidAIPlayer(moves_service, symbol)
            case 2:
                self.__ai = NormalAIPlayer(moves_service, symbol)
            case _:
                self.__ai = SmartAIPlayer(moves_service, symbol)
    
    def make_move(self):
        self.computer.make_move()
    
    @property
    def computer(self):
        return self.__ai

class StupidAIPlayer:
    def __init__(self, moves_service:MoveService, symbol:str):
        self._moves_service = moves_service
        self._symbol = symbol
    
    def make_move(self):
        x = random.randint(0, 5)
        y = random.randint(0, 5)

        while(self._moves_service.board[x, y] != ' '):
            x = random.randint(0, 5)
            y = random.randint(0, 5)
        
        self._moves_service.mark(x, y, self._symbol)
        

class SmartAIPlayer(StupidAIPlayer):

    __weight = [[0.1, 0.2, 0.2, 0.2, 0.2, 0.1], [0.2, 0.4, 0.4, 0.4, 0.4, 0.2], [0.2, 0.4, 0.7, 0.7, 0.4, 0.2],
               [0.2, 0.4, 0.7, 0.7, 0.4, 0.2], [0.2, 0.4, 0.4, 0.4, 0.4, 0.2], [0.1, 0.2, 0.2, 0.2, 0.2, 0.1]]
    def __init__(self, moves_service:MoveService, symbol:str):
        super().__init__(moves_service, symbol)

    def make_move(self):
        best_eval = int(-1e9) if self._symbol == 'O' else int(1e9)
        best_move = None
        is_maximizing = (self._symbol == 'O') # True if we are the max player, False otherwise
        sign = 1 if is_maximizing else -1
        candidate_cells = self._get_best_candidate_cells() if len(self._moves_service.board.free_cells) == 36 else self._moves_service.board.free_cells[:]

        for x, y in candidate_cells:
            self._moves_service.mark(x, y, self._symbol)
            eval = self.minimax(not is_maximizing, int(-1e9), int(1e9)) + sign * ((36 - len(self._moves_service.board.free_cells)) + SmartAIPlayer.__weight[x][y])
            self._moves_service.undo()

            if (is_maximizing and eval > best_eval) or (not is_maximizing and eval < best_eval):
                best_eval = eval
                best_move = (x, y)
        
        self._moves_service.mark(best_move[0], best_move[1], self._symbol)

    def minimax(self, max_player:bool, alpha:int, beta:int):
        if self._terminal_state() == True:
            return self._static_eval_function(max_player)
        
        candidate_cells = self._moves_service.board.free_cells[:]
        
        if max_player == True:
            max_eval = int(-1e9)
            for x, y in candidate_cells:
                self._moves_service.mark(x, y, 'O')
                eval = self.minimax(False, alpha, beta)
                max_eval = max(max_eval, eval)

                alpha =  max(max_eval, eval)
                if alpha >= beta:
                    self._moves_service.undo() 
                    break

                self._moves_service.undo() 
            return max_eval
        else:
            min_eval = int(1e9)
            for x, y in candidate_cells:
                self._moves_service.mark(x, y, 'X')
                eval = self.minimax(True, alpha, beta)
                min_eval = min(min_eval, eval)

                beta = min(min_eval, eval)
                if alpha >= beta:
                    self._moves_service.undo()
                    break

                self._moves_service.undo()
            return min_eval

    def _terminal_state(self):
        return len(self._moves_service.board.free_cells) == 0

    # returns 1 if on a state of the board the first player wins, -1 otherwise
    def _static_eval_function(self, max_player:bool):
        return 1000 if not max_player == True else -1000
    
    def _get_best_candidate_cells(self):
        candidate_cells = self._moves_service.board.filter_symmetric_positions()[:]
        for x, y in candidate_cells[:]:
            if x == 0 or x == 5 or y == 0 or y == 5:
                candidate_cells.remove((x, y))
        return candidate_cells

class NormalAIPlayer(SmartAIPlayer):
    def __init__(self, moves_service:MoveService, symbol:str):
        super().__init__(moves_service, symbol)
    
    def make_move(self):
        best_eval = int(-1e9) if self._symbol == 'O' else int(1e9)
        best_move = None
        is_maximizing = (self._symbol == 'O') # True if we are the max player, False otherwise
        candidate_cells = self._get_best_candidate_cells() if len(self._moves_service.board.free_cells) == 36 else self._moves_service.board.free_cells[:]

        for x, y in candidate_cells:
            self._moves_service.mark(x, y, self._symbol)
            eval = self.minimax(not is_maximizing, int(-1e9), int(1e9))
            self._moves_service.undo()

            if (is_maximizing and eval > best_eval) or (not is_maximizing and eval < best_eval):
                best_eval = eval
                best_move = (x, y)
        
        self._moves_service.mark(best_move[0], best_move[1], self._symbol)
    

# board = Board()
# move = MoveService(board)

# ai1 = SmartAIPlayer(move, 'O')
# ai2 = NormalAIPlayer(move, 'O')
# ai3 = StupidAIPlayer(move, 'O')

# move.mark(2, 2, 'O')
# move.mark(4, 4, 'O')
# move.mark(5, 1, 'O')
# move.mark(5, 0, 'X')


#ai1.make_move()
#ai1.make_move()
#ai1.make_move()
#print(board)