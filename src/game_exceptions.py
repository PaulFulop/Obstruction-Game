#Parent exception
class GameException(Exception):
    pass

class OutOfBoardError(GameException):
    def __init__(self):
        super().__init__("Out of board.")

class OccpiedCellError(GameException):
    def __init__(self, x:int, y:int):
        super().__init__(f"The cell at row {x} and column {y} is already occupied.")

class GameOverError(GameException):
    def __init__(self, current_player:str):
        super().__init__(f"{current_player} won!")