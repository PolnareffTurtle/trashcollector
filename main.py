import pygame
from sys import exit

class Game:

    #this is a list of all the gamestates that the game switches between
    GAME_RUNNING = 0
    MAIN_MENU = 1

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960,720))
        self.clock = pygame.time.Clock()
        self.gamestate = Game.MAIN_MENU

    def main_menu(self):
        while self.gamestate == Game.MAIN_MENU:
            self.screen.fill((120,24,100))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.gamestate = Game.GAME_RUNNING
                        break

            if self.gamestate == Game.MAIN_MENU:
                self.clock.tick(60)
                pygame.display.update()

    def game_running(self):
        while self.gamestate == Game.GAME_RUNNING:
            self.screen.fill((200,50,50)) #TODO: change this to the background image

            #player keyboard input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.clock.tick(60)
            pygame.display.update()

    def run(self):
        while True:
            if self.gamestate == Game.MAIN_MENU:
                self.main_menu()
            elif self.gamestate == Game.GAME_RUNNING:
                self.game_running()

if __name__ == '__main__':
    game = Game()
    game.run()