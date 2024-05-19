import pygame
import json

NEIGHBOR_OFFSETS = [
    (-1,-1), (0,-1), (1,-1), (2,-1),
    (-1,0),  (0,0),  (1,0),  (2,0),
    (-1,1),  (0,1),  (1,1),  (2,1),
    (-1,2),  (0,2),  (1,2),  (2,2)
]

COLLIDE_RECTS = list(range(20))+list(range(22,42))+list(range(44,64))+list(range(66,86))+list(range(88,176))+list(range(184,194))+list(range(206,216))\
                +list(range(10))




class Tile:
    def __init__(self,tile_index,pos):
        self.index = tile_index
        self.pos = pos