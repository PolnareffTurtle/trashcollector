import pygame
import json

NEIGHBOR_OFFSETS = [
    (-1,-1), (0,-1), (1,-1), (2,-1),(3,-1),
    (-1,0),  (0,0),  (1,0),  (2,0), (3,0),
    (-1,1),  (0,1),  (1,1),  (2,1), (3,1),
    (-1,2),  (0,2),  (1,2),  (2,2), (3,2),
]

COLLIDE_TILES = list(range(20))+list(range(22,42))+list(range(44,64))+list(range(66,86))+list(range(88,176))+list(range(184,194))+list(range(206,216))+list(range(220,560))

LOSE_TILES = list(range(568,576))

WIN_TILES = None

class Tile:
    def __init__(self,tile_index,pos):
        self.index = tile_index
        self.pos = pos

class Tilemap:
    def __init__(self, game, level, tile_size=16):
        self.game = game
        self.tilemaps = []
        self.tile_size = tile_size
        self.torches = []
        self.open_json(level)

    def open_json(self,level):
        with open('data/levels/'+str(level)+'.json') as f:
            rawdata = f.read()
            jsondata = json.loads(rawdata)


        self.main_layer = jsondata['properties'][0]['value']
        self.size = (jsondata['width'],jsondata['height'])

        for layer in jsondata['layers']:
            tilemap = {}
            for j, val in enumerate(layer['data']):
                if val != 0:
                    tilemap[(j%layer['width'],j//layer['width'])] = Tile(val-1,(j%layer['width'],j//layer['width']))
            self.tilemaps.append(tilemap)

    def tiles_around(self,pos):
        tiles = []
        for offset in NEIGHBOR_OFFSETS:

            check = (pos[0]//self.tile_size+offset[0],pos[1]//self.tile_size+offset[1])
            if check in self.tilemaps[self.main_layer]:

                tiles.append(self.tilemaps[self.main_layer][check])
        return tiles

    def physics_rects_around(self,pos):
        physics_rects = {'collide':[],'win':[],'lose':[]}
        for tile in self.tiles_around(pos):
            tile_rect = pygame.rect.Rect(tile.pos[0]*self.tile_size,tile.pos[1]*self.tile_size,self.tile_size,self.tile_size)
            if tile.index in COLLIDE_TILES:
                print(tile.index)
                physics_rects['collide'].append(tile_rect)
            elif tile.index in WIN_TILES:
                physics_rects['win'].append(tile_rect)
            elif tile.index in LOSE_TILES:
                physics_rects['lose'].append(tile_rect)
        return physics_rects

    def render(self,surf,offset=(0,0)):
        for tilemap in self.tilemaps:
            for x in range(offset[0]//self.tile_size,(offset[0]+surf.get_width())//self.tile_size+1):
                for y in range(offset[1]//self.tile_size,(offset[1]+surf.get_height())//self.tile_size+1):
                    if (x,y) in tilemap:
                        tile = tilemap[(x,y)]
                        surf.blit(self.game.assets['tiles'][tile.index],(tile.pos[0]*self.tile_size-offset[0],tile.pos[1]*self.tile_size-offset[1]))
                        pygame.draw.rect(surf, 'blue', (
                        tile.pos[0] * self.tile_size - offset[0], tile.pos[1] * self.tile_size - offset[1],
                        self.tile_size, self.tile_size), 1)