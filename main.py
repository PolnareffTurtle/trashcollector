import pygame
from sys import exit
from scripts.utils import Text,load_image,load_images,Animation
from scripts.entities import Player

class Game:

    #this is a list of all the gamestates that the game switches between
    GAME_RUNNING = 0
    MAIN_MENU = 1

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080,720))
        self.display = pygame.Surface((360, 240))
        self.clock = pygame.time.Clock()
        self.gamestate = Game.MAIN_MENU
        self.assets = {
            'player': load_image('player/gojo.png') #TODO: add the new player image
        }

        self.player = Player(self,(100,-100))

    def main_menu(self):
        while self.gamestate == Game.MAIN_MENU:
            self.display.fill((120,24,100))

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
                self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()),(0,0))

    def game_running(self):
        self.movement = [False, False]

        while self.gamestate == Game.GAME_RUNNING:
            self.display.fill((200,50,50)) #TODO: change this to the background image

            self.player.update((self.movement[1]-self.movement[0],0))
            self.player.render(self.display)

            #player keyboard input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_LEFT, pygame.K_a]:
                        self.movement[0] = True
                    if event.key in [pygame.K_RIGHT, pygame.K_d]:
                        self.movement[1] = True
                    if event.key in [pygame.K_UP, pygame.K_w, pygame.K_SPACE]:
                        self.player.jump()
                    if event.key == pygame.K_ESCAPE:
                        self.gamestate = Game.MAIN_MENU
                        break

                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT, pygame.K_a]:
                        self.movement[0] = False
                    if event.key in [pygame.K_RIGHT, pygame.K_d]:
                        self.movement[1] = False
                    if event.key == pygame.K_j:
                        self.player.shift = 0



            self.clock.tick(60)
            pygame.display.update()
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

    def run(self):
        while True:
            if self.gamestate == Game.MAIN_MENU:
                self.main_menu()
            elif self.gamestate == Game.GAME_RUNNING:
                self.game_running()

if __name__ == '__main__':
    game = Game()
    game.run()