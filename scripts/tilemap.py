import pygame
import json
import re

NEIGHBOR_OFFSETS = [
    (-1,-1), (0,-1), (1,-1), (2,-1),(3,-1),
    (-1,0),  (0,0),  (1,0),  (2,0), (3,0),
    (-1,1),  (0,1),  (1,1),  (2,1), (3,1),
    (-1,2),  (0,2),  (1,2),  (2,2), (3,2),
]


WIN_TILES = [3,4,6,7]

TRASH_TILES = [0,1,2,5,8]

class Tile:
    def __init__(self,tile_index,pos,tileset):
        self.index = tile_index
        self.pos = pos
        self.tileset = tileset

class Tilemap:
    def __init__(self, game, level, tile_size=16):
        self.game = game
        self.tilemaps = []
        self.tile_size = tile_size
        self.torches = []
        self.open_json(level)

    def tile_id(self,val,tilesets):
        for tileset in tilesets[::-1]:
            if val >= tileset['firstgid']:
                # [local value of tile within tileset, tileset name (ex. "trash")]
                return [val-tileset['firstgid'], re.search('([A-Za-z0-9]+)\.tsx',tileset['source']).group(1)]


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
                    tile_id = self.tile_id(val,jsondata['tilesets'])
                    #tile at [locationx, locationy] = Tile(local id, pos, tileset)
                    tilemap[(j%layer['width'],j//layer['width'])] = Tile(tile_id[0],(j%layer['width'],j//layer['width']),tile_id[1])
            self.tilemaps.append(tilemap)

    def tiles_around(self,pos):
        tiles = []
        for offset in NEIGHBOR_OFFSETS:

            check = (pos[0]//self.tile_size+offset[0],pos[1]//self.tile_size+offset[1])
            if check in self.tilemaps[self.main_layer]:

                tiles.append(self.tilemaps[self.main_layer][check])
        return tiles

    def physics_rects_around(self,pos):
        physics_rects = {'collide':[],'win':[],'lose':[],'trash':[]}
        for tile in self.tiles_around(pos):
            tile_rect = pygame.rect.Rect(tile.pos[0]*self.tile_size,tile.pos[1]*self.tile_size,self.tile_size,self.tile_size)
            if tile.tileset in ['blue','yellow']:
                physics_rects['collide'].append(tile_rect)
            elif tile.tileset == 'trash':
                if tile.index in WIN_TILES:
                    physics_rects['win'].append(tile_rect)
                else:
                    physics_rects['trash'].append(tile_rect)
            elif tile.tileset == 'spike':
                physics_rects['lose'].append(tile_rect)
        return physics_rects

    def render(self,surf,offset=(0,0)):
        for tilemap in self.tilemaps:
            for x in range(offset[0]//self.tile_size,(offset[0]+surf.get_width())//self.tile_size+1):
                for y in range(offset[1]//self.tile_size,(offset[1]+surf.get_height())//self.tile_size+1):
                    if (x,y) in tilemap:

                        tile = tilemap[(x,y)]
                        print(tile.tileset,tile.index)

                        surf.blit(self.game.assets['tiles'][tile.tileset][tile.index],(tile.pos[0]*self.tile_size-offset[0],tile.pos[1]*self.tile_size-offset[1]))
                        #pygame.draw.rect(surf, 'blue', (
                        #tile.pos[0] * self.tile_size - offset[0], tile.pos[1] * self.tile_size - offset[1],
                        #self.tile_size, self.tile_size), 1)