import pygame

class Player:
    def __init__(self,game,pos):
        self.game = game
        self.pos = list(pos)
        self.animation = self.game.assets['player_walk']
        self.velocity = [0,0]

    #this part is for detecting player movement/collisions/interactions
    def update(self,movement): #"movement" is player input from keyboard
        frame_movement = [movement[0]+self.velocity[0],movement[1]+self.velocity[1]] #velocity is for jumping

        self.pos[1] += frame_movement[1] #this is checking frame movement for vertical movement first

        self.pos[0] += frame_movement[0] #then it moves the player horizontally to check

        self.velocity[1] = min(10, self.velocity[1] + 0.25)

        player_rect = self.rect()

        self.animation.update()

        if player_rect.bottom > 200:
            player_rect.bottom = 200
            self.pos[1] = player_rect.y
            self.velocity[1] = 0

    def jump(self):
        self.velocity[1] = -5

    def render(self,surf):
        surf.blit(self.animation.img(),self.pos)

    def rect(self):
        return pygame.rect.Rect(self.pos, self.animation.img().get_size())