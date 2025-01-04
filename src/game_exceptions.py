# Custom game exceptions

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

class PropertiesError(GameException):
    def __init__(self):
        super().__init__("The settings.properties file has incomplete/invalid information about the game properties or it doesn't exist.")