import pygame
import os

BASE_IMG_PATH = 'data/graphics/'


#this just loads the image
def load_image(path,alpha=True,scale=None):

    if alpha:
        img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
    else:

        img = pygame.image.load(BASE_IMG_PATH + path).convert()
        img.set_colorkey((0, 0, 0))
    if scale:
        img = pygame.transform.scale_by(img,scale)


    return img

#creates images from a folder of images; it might not work on windows because mac is different with os
def load_images(path,alpha=True,scale=None):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        if img_name == '.DS_Store':
            continue
        images.append(load_image(path + '/' + img_name, alpha,scale))
    return images

#an Animation is a collection of images that has the function "update" and can return its current frame with "Iimg"
class Animation:
    def __init__(self,images,duration,loop=True):
        self.images = images
        self.duration = duration
        self.loop = loop
        self.frame_index = 0


    def update(self):
        self.frame_index = (self.frame_index+1)%(self.duration*len(self.images))

    def img(self):
        return self.images[self.frame_index//self.duration]

#Text can instantly render text if "surf" and "pos" is provided, otherwise it also has a render function
class Text:
    def __init__(self,text,size,color,surf=None,pos=None):
        self.font = pygame.font.Font('arial',size)
        self.image = self.font.render(text,False,color)
        if surf and pos:
            surf.blit(self.image,pos)
    def render(self,surf,pos):
        surf.blit(self.image, pos)