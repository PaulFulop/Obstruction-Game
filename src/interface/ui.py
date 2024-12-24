# For playing in the console

import sys
sys.path.append("./src")
from services.game_service import GameService, Players

class UI:
    def __init__(self, firstPlayer:Players):
        self.__game = GameService(firstPlayer)
    
    @staticmethod
    def display_commands():
        print("List of commands:\n\n"
              "start -> start a new round\n"
              "score -> show the score\n"
              "exit -> exit the game\n")