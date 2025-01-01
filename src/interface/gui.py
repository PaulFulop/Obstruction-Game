import pygame 

import sys
sys.path.append("./src")
from game_init import GameInit, Players
from game_exceptions import GameOverError

class GUI:
    WHITE = (255, 255, 255)
    BACKGROUND_COLOR = (40, 44, 52)
    startX, startY = 25, 40
    cell_size = 80

    def __init__(self, firstPlayer:Players, difficulty:int):
        self.__game = GameInit(firstPlayer, difficulty)
        self.__screen = pygame.display.set_mode((800, 600))
        pygame.init()

        icon = pygame.image.load("src/explosion.png")
        pygame.display.set_icon(icon)

    def display_human_move(self, x:int, y:int):
        self.__game.human.make_move(x, y)
        self.__game.state.record_state(self.__game.board, False)
    
    def display_computer_move(self):
        self.__game.computer.make_move()
        self.__game.state.record_state(self.__game.board, True)
    
    def run(self):
        pygame.display.set_caption("Obliteration Game")
        turn = self.__game.flag
        game_over = False
        while True:
            self.__screen.fill(GUI.BACKGROUND_COLOR)
            self.__game.board.draw(self.__screen, GUI.startX, GUI.startY, GUI.cell_size)
            pygame.display.update()

            if turn and not game_over:
                try:
                    self.display_computer_move()
                    turn = not turn  
                except GameOverError as goe:
                    turn = self.__game.flag
                    game_over = True
                    print(str(goe))

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not turn and not game_over:
                        posX, posY = event.pos
                        posX -= GUI.startX  
                        posY -= GUI.startY
                        posX //= GUI.cell_size
                        posY //= GUI.cell_size
                    elif turn:
                        pygame.event.get().remove(event)

                    try:
                        self.display_human_move(posY, posX)
                        turn = not turn
                        print("Left-click detected at", posY, posX)
                    except GameOverError as goe:
                        turn = self.__game.flag
                        print(str(goe))
                    except Exception as e:
                        print(str(e))


gui = GUI(Players.HUMAN_PLAYER, 2) 
gui.run()