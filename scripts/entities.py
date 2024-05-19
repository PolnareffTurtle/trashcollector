import pygame

class Player:
    def __init__(self,game,pos):
        self.game = game
        self.pos = list(pos)
        self.animation = self.game.assets['player_walk']
        self.velocity = [0,0]

        self.air_time=0
        self.jumps=0

    #this part is for detecting player movement/collisions/interactions
    def update(self,tilemap,movement=(0,0)): #"movement" is player input from keyboard
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}
        frame_movement = [2*movement[0]+self.velocity[0],2*movement[1]+self.velocity[1]] #velocity is for jumping
        rects = tilemap.physics_rects_around(self.pos)

        self.pos[1] += frame_movement[1] #this is checking frame movement for vertical movement first

        self_rect = self.rect()
        for rect in rects['collide']:
            if self_rect.colliderect(rect):

                if frame_movement[1] > 0:
                    print('VERTICSL')
                    self_rect.bottom = rect.top
                    self.collisions['down'] = True


                elif frame_movement[1] < 0:
                    self_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = self_rect.y

        self.pos[0] += frame_movement[0] #then it moves the player horizontally to check

        self_rect = self.rect()
        for rect in rects['collide']:
            if self_rect.colliderect(rect):
                print('asdfoaisjdfoi')

                if frame_movement[0] > 0:

                    self_rect.right = rect.left
                    self.collisions['right'] = True

                elif frame_movement[0] < 0:
                    self_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = self_rect.x

        for rect in rects['win']:
            if self_rect.colliderect(rect):
                self.game.gamestate = self.game.WIN
        for rect in rects['lose']:
            if self_rect.collidepoint(rect.center):
                self.game.gamestate = self.game.LOSE
        for rect in rects['trash']:
            if self_rect.colliderect(rect):
                self.game.trash_current_level += 1
                del tilemap.tilemaps[tilemap.main_layer][(rect.x//tilemap.tile_size,rect.y//tilemap.tile_size)]

        if self.collisions['up'] or self.collisions['down']:
            self.velocity[1] = 0
        if self.collisions['down']:
            self.air_time = 0
            self.jumps = 1

        self.air_time += 1
        if self.air_time > 4:
            self.jumps = 0

        self.velocity[1] = min(10, self.velocity[1] + 0.25)

        self.animation.update()

        if self_rect.bottom > tilemap.size[1]*tilemap.tile_size:
            self.game.gamestate = self.game.LOSE

    def jump(self):
        if self.jumps:
            self.velocity[1] = -5

    def render(self,surf,offset=(0,0)):
        surf.blit(self.animation.img(),(self.pos[0]-offset[0],self.pos[1]-offset[1]))
        #pygame.draw.rect(self.game.display, (0, 0, 255),pygame.rect.Rect(self.pos[0]-offset[0], self.pos[1]-offset[1], self.animation.img().get_width(), self.animation.img().get_height()),width=1)

    def rect(self):

        return pygame.rect.Rect(list(self.pos), (40,26))