import pygame
from sys import exit
from scripts.utils import Text,load_image,load_images,Animation
from scripts.entities import Player

class Game:

    #this is a list of all the gamestates that the game switches between
    GAME_RUNNING = 0
    MAIN_MENU = 1
    LEVEL_SELECT = 2
    OPTIONS = 3
    GAME_MENU = 4

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080,720))
        pygame.display.set_caption('Crab Conservation Corps')
        self.display = pygame.Surface((360, 240))
        self.clock = pygame.time.Clock()
        self.gamestate = Game.MAIN_MENU
        self.assets = {
            'player_walk': Animation(load_images('player/walk'),5), #TODO: add the new player image
            'background': load_image('beach.png'),
            'background2': load_image('beach2.png')
        }

        self.player = Player(self,(100,-100))

    def main_menu(self):
        #self.background = pygame.Surface((1080,720))
        option_index = 0
        while self.gamestate == Game.MAIN_MENU:
            self.display.blit(self.assets['background2'],(0,0))

            option_select = pygame.Surface((180, 28))
            option_select.fill((0, 0, 0))

            option_select.set_alpha(100)
            self.display.blit(option_select, (90, 101 + option_index * 30))

            Text('Crab Conservation Corps', 24, 'black', self.display, (49, 11))
            Text('Crab Conservation Corps',24,'white',self.display,(50,10))

            Text('Play',24,'black',self.display,(159,101))
            Text('Play', 24, 'white', self.display, (160, 100))
            Text('Levels', 24, 'black', self.display, (149, 131))
            Text('Levels', 24, 'white', self.display, (150, 130))
            Text('Options', 24, 'black', self.display, (143, 161))
            Text('Options', 24, 'white', self.display, (144, 160))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        option_index = (option_index - 1) % 3
                    elif event.key == pygame.K_DOWN:
                        option_index = (option_index + 1) % 3
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.gamestate = [Game.GAME_RUNNING, Game.LEVEL_SELECT, Game.OPTIONS][option_index]
                        break


            if self.gamestate == Game.MAIN_MENU:
                self.clock.tick(60)
                pygame.display.update()
                self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()),(0,0))

    def game_running(self):
        self.movement = [False, False]


        while self.gamestate == Game.GAME_RUNNING:
            self.display.blit(self.assets['background'],(0,0)) #TODO: change this to the background image

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
            self.display = pygame.Surface((360, 240))
            if self.gamestate == Game.MAIN_MENU:
                self.main_menu()
            elif self.gamestate == Game.GAME_RUNNING:
                self.game_running()

if __name__ == '__main__':
    game = Game()
    game.run()