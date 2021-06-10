import pygame
import json
from settings import *

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename # allows you to choose a filename
        # changes the filename to a format pygame can work with
        self.sprite_sheet = pygame.image.load(filename).convert()
        # replaces png file with json file extension
        self.meta_data = self.filename.replace('png', 'json')

        with open(self.meta_data) as f:
            self.data = json.load(f)
        

    def get_sprite(self, x, y, w, h):
        # assigns a width and a height that's equal to the one in the json file
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey(BLACK)
        # blits the part of the spritesheet onto the surface
        # using the assigned coordinates
        sprite.blit(self.sprite_sheet, (0, 0), (x,y, w, h))

        return sprite
    
    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame'] # slice json file 
        x, y, w, h = sprite['x'], sprite['y'], sprite['w'], sprite['h']# assign x, y, w, h to sprite
        image = self.get_sprite(x, y, w, h) # assign sliced data to image

        return image