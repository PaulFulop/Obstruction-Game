# For playing in the console

import sys, os, time
sys.path.append("./src")
from game_init import GameInit, Players
from repository.score_repo import ScoreRepo
from prettytable import PrettyTable
from game_exceptions import GameOverError

# TODO fix txt repo problem
class UI:
    def __init__(self, firstPlayer:Players):
        self.__game = GameInit(firstPlayer)
        self.__score_repo = ScoreRepo("src/repository/score.txt")
        self.__first_player_info = "(you will play first)" if self.__game.flag == False else "(the computer will play first)"

    def display_commands(self):
        print("OBSTRUCTION GAME\n\n"
              "List of commands:\n\n"
              f"start -> start a new round {self.__first_player_info}\n"
              "score -> show the score\n"
              "exit -> exit the game\n") 
    
    @staticmethod
    def clear_console():
        os.system("cls")

    def redraw_console(self, message:str):
        UI.clear_console()
        self.display_commands()
        print(message + '\n')

    def display_human_move(self):
        self.redraw_console(str(self.__game.board))
        pos = input("Insert the position you want to mark here: ")
        tokens = pos.split()
        x = int(tokens[0].strip())
        y = int(tokens[1].strip())
        self.__game.human.make_move(x, y)

    def display_computer_move(self):
        self.redraw_console(str(self.__game.board))
        print("Computer thinking...")
        time.sleep(2)
        self.__game.computer.make_move()
    
    def run(self):
        message = " "

        while True:
            self.redraw_console(message)
            cmd = input("> ")

            match cmd.lower().strip():
                case "start":
                    if self.__game.flag == False:
                        while True:
                            try:
                                self.display_human_move()
                                self.display_computer_move()
                            except GameOverError as goe:
                                message = str(self.__game.board) + '\n\n' + str(goe)
                                break
                            except Exception as e:
                                print(e)
                                time.sleep(2.5)
                                pass
                    else:
                        while True:
                            try:
                                self.display_computer_move()
                                self.display_human_move()
                            except GameOverError as goe:
                                message = str(self.__game.board + '\n\n' + goe)
                                break
                            except Exception as e:
                                print(e)
                                time.sleep(2.25)
                                pass
                case "score":
                    try:
                        tokens = self.__score_repo.data
                        h_points, c_points = tokens[0], tokens[1]
                        
                        table = PrettyTable(("human", "computer"))
                        table.add_row([h_points, c_points])
                        message = str(table)
                    except ValueError as ve:
                        message = str(ve)
                case "exit":
                    print("Exiting...\n")
                    break
                case _:
                    message = "Invalid command.\n"
                    
ui = UI(Players.HUMAN_PLAYER)
ui.run()