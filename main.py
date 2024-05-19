import pygame
from sys import exit
from scripts.utils import Text,load_image,load_images,Animation
from scripts.entities import Player
from scripts.tilemap import Tilemap
from scripts.texts import texts

class Game:

    #this is a list of all the gamestates that the game switches between
    GAME_RUNNING = 0
    MAIN_MENU = 1
    LEVEL_SELECT = 2
    OPTIONS = 3
    GAME_MENU = 4
    WIN = 5
    LOSE = 6

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080,720))
        pygame.display.set_caption('Crustacean Conservation Corps')
        self.display = pygame.Surface((360, 240))
        self.clock = pygame.time.Clock()
        self.gamestate = Game.LEVEL_SELECT
        self.trash_current_level=0
        self.option_index = [0, 0]
        self.option = 0

        self.assets = {
            'player_walk': Animation(load_images('player/walk'),5), #TODO: add the new player image
            'background': load_image('bestbackground.png'),
            'background2': load_image('gradient.png'),
            'tiles': load_images('tiles/1_blue')+load_images('tiles/0_yellow')+load_images('tiles/6_trash')+load_images('tiles/2_spike')+load_images('tiles/4_grass')+
                     load_images('tiles/5_tree')+load_images('tiles/3_rock'),
        }

        print(len(self.assets['tiles']))


        self.level = 1
        self.trash = [0,0,0,0,0,0]
        self.total_trash = [10,10,10,10,10,10]


    def main_menu(self):
        option_index = 0

        while self.gamestate == Game.MAIN_MENU:
            self.display.blit(self.assets['background2'],(0,0))
            Text('CONSERVATION CORPS', 100, 'white', self.display, (-50, -720), 30,alpha=100)

            Text('CRAB CONSERVATION CORPS',100,'white',self.display,(-500,-500),30,alpha=100)
            Text('ATION', 100, 'white', self.display, (60, 65), 30, alpha=100)

            pygame.draw.rect(self.display, 'white', (134, 132 + (option_index % 3) * 34, 300, 34), 0)
            #pygame.draw.rect(self.display,'white',(0,10,330,100),0)

            Text('Crustacean', 30, 'black', self.display, (20, 11))
            Text('Conservation', 30, 'black', self.display, (20, 41))
            Text('Corps', 30, 'black', self.display, (20, 71))

            Text('Play',30,'black',self.display,(160,130))
            Text('Levels', 30, 'black', self.display, (160, 164))
            Text('Options', 30, 'black', self.display, (160, 198))

            #Text('V', 20, 'black', self.display, (134, 136 + (option_index % 3) * 34), 90)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        option_index = (option_index - 1) % 3
                    elif event.key == pygame.K_DOWN:
                        option_index = (option_index + 1) % 3
                    elif event.key == pygame.K_RETURN:
                        self.gamestate = [Game.GAME_MENU, Game.LEVEL_SELECT, Game.OPTIONS][option_index]
                        break




            if self.gamestate == Game.MAIN_MENU:
                self.clock.tick(60)
                pygame.display.update()
                self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()),(0,0))

    def level_select(self):
        option_index = 0
        while self.gamestate == Game.LEVEL_SELECT:
            self.display.blit(self.assets['background2'],(0,0))

            Text('ESC', 10, 'black', self.display, (10, 10))

            pygame.draw.rect(self.display, 'white',
                             (68 + (option_index % 3) * 82, 40 + (option_index // 3) * 60, 80, 50), 0)

            Text('1       2       3',30,'black',self.display,(90,40))
            Text('4       5       6', 30, 'black', self.display, (90, 100))

            for i in range(6):
                Text(str(self.trash[i])+ ' of ' + str(self.total_trash[i]),10,'black',self.display,(78+(i%3)*82,74+(i//3)*60,))


            #Text('V', 20, 'black', self.display, (62 + (option_index % 3) * 80, 50 + (option_index // 3) * 60),90)
            #Text('>', 15, 'black', self.display, (90 + (option_index % 3) * 72, 28 + (option_index // 3) * 40))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        option_index = (option_index-3)%6
                    elif event.key == pygame.K_DOWN:
                        option_index = (option_index+3)%6
                    elif event.key == pygame.K_LEFT:
                        option_index = (option_index-1)%6
                    elif event.key == pygame.K_RIGHT:
                        option_index = (option_index+1)%6
                    elif event.key == pygame.K_RETURN:
                        self.level = option_index+1
                        self.gamestate = Game.GAME_MENU
                        break
                    elif event.key == pygame.K_ESCAPE:
                        self.gamestate = Game.MAIN_MENU
                        break

            if self.gamestate == Game.LEVEL_SELECT:
                self.clock.tick(60)
                pygame.display.update()
                self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

    def options(self):
        while self.gamestate == Game.OPTIONS:
            self.display.blit(self.assets['background2'],(0,0))
            pygame.draw.rect(self.display, 'white', (0, 30 + self.option * 30, 350, 30), 0)
            Text('[ESC]', 10, 'black', self.display, (5, 5))
            Text('Sound', 20, 'black', self.display, (10, 30))
            Text('Resolution', 20, 'black', self.display, (10, 60))
            Text(['On', 'Off'][self.option_index[0]], 20, 'black', self.display, (200, 30))
            Text(['1080x720', '1440x960', '360x240','720x480'][self.option_index[1]], 20, 'black', self.display, (200, 60))
            Text('>', 20, 'black', self.display, (5, 15 + self.option * 20))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYUP:
                    if event.key in [pygame.K_UP,pygame.K_DOWN]:
                        self.option=(self.option+1)%2
                    if event.key == pygame.K_RIGHT:
                        self.option_index[self.option] = (self.option_index[self.option]+1)%[2,4][self.option]
                        if self.option ==1:
                            pygame.display.set_mode([(1080,720), (1440, 960), (360, 240),(720, 480)][self.option_index[1]])

                    elif event.key == pygame.K_LEFT:
                        self.option_index[self.option] = (self.option_index[self.option]-1)%[2,4][self.option]
                        if self.option == 1:
                            pygame.display.set_mode([(1080,720), (1440, 960),  (360, 240),(720, 480)][self.option_index[1]])

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.gamestate = Game.MAIN_MENU
                        break

            self.clock.tick(60)
            pygame.display.update()
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

    def game_menu(self):
        while self.gamestate == Game.GAME_MENU:
            self.display.blit(self.assets['background2'],(0,0))

            texts(self.display,'game_menu',self.level)

            Text('ESC', 10, 'black', self.display, (10, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.gamestate = Game.MAIN_MENU
                        break
                    else:
                        self.gamestate = Game.GAME_RUNNING
                        break

            self.clock.tick(60)
            pygame.display.update()
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

    def game_running(self):
        self.player = Player(self, (100, 0))
        self.movement = [False, False]
        self.scroll = [self.player.rect().centerx - self.display.get_width() / 2,
                       self.player.rect().centery - self.display.get_height() / 2]
        self.tilemap = Tilemap(self, self.level)

        self.trash_current_level = 0


        while self.gamestate == Game.GAME_RUNNING:
            #scroll is for the camera, slowly locks into the player as the center
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 10
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 10
            self.render_scroll = [int(self.scroll[0]), int(self.scroll[1])]

            self.display.blit(self.assets['background'],(0,0))

            self.tilemap.render(self.display, offset=self.render_scroll)
            self.player.update(self.tilemap,(self.movement[1]-self.movement[0],0))
            self.player.render(self.display,offset=self.render_scroll)

            Text('ESC',10, 'black', self.display, (10, 10))

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


                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT, pygame.K_a]:
                        self.movement[0] = False
                    if event.key in [pygame.K_RIGHT, pygame.K_d]:
                        self.movement[1] = False
                    if event.key == pygame.K_ESCAPE:
                        self.gamestate = Game.MAIN_MENU
                        break
                    if event.key == pygame.K_r:
                        self.gamestate = Game.GAME_MENU

            self.clock.tick(60)
            pygame.display.update()
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

    def win(self):
        self.trash[self.level - 1] = max(self.trash_current_level,
                                         self.trash[self.level - 1])  # add to the trash if it is greater
        while self.gamestate == Game.WIN:
            self.display.blit(self.assets['background2'],(0,0))
            Text('You collected',20,'black',self.display,(72,20))
            Text(str(self.trash_current_level) + ' out of ' + str(self.total_trash[self.level - 1]),30,'black',self.display,(70,50))
            Text('pieces of trash', 20, 'black', self.display,(68,96))

            Text('Press R to Restart',10,'black',self.display,(50,150))
            Text('Press ENTER for Next Level', 10, 'black', self.display, (50, 165))
            Text('Press ESC to exit', 10, 'black', self.display, (50, 180))

            Text('ESC', 10, 'black', self.display, (10, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_r:
                        self.gamestate = Game.GAME_MENU
                        break
                    elif event.key == pygame.K_ESCAPE:
                        self.gamestate = Game.MAIN_MENU
                        break
                    elif event.key == pygame.K_RETURN:
                        if self.level < 6:
                            self.level += 1
                            self.gamestate = Game.GAME_MENU
                        elif self.level == 6:
                            self.gamestate = Game.MAIN_MENU
                        break

            self.clock.tick(60)
            pygame.display.update()
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))



    def lose(self):
        self.gamestate = Game.GAME_MENU

    def run(self):
        while True:
            self.display = pygame.Surface((360, 240))
            if self.gamestate == Game.MAIN_MENU:
                self.main_menu()
            elif self.gamestate == Game.LEVEL_SELECT:
                self.level_select()
            elif self.gamestate == Game.OPTIONS:
                self.options()
            elif self.gamestate == Game.GAME_RUNNING:
                self.game_running()
            elif self.gamestate == Game.GAME_MENU:
                self.game_menu()
            elif self.gamestate == Game.LOSE:
                self.lose()
            elif self.gamestate == Game.WIN:
                self.win()

if __name__ == '__main__':
    game = Game()
    game.run()