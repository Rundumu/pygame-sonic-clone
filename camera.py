import pygame
from settings import *
from abc import ABC, abstractmethod

vector = pygame.math.Vector2

class Camera:
    def __init__(self, player):
        self.player = player
        self.offset = vector(0, 0) # frames camera position
        self.offset_float = vector(0, 0) # store precise camera position
        self.width, self.height = WIDTH, HEIGHT
        self.CONST = vector(-self.width / 2 + player.pos.x, -player.pos.y + 20)

    def setmethod(self, method): # picks which method to use
        self.method = method
    
    def scroll(self): # performs calculations on the chosen method
        self.method.scroll()

class CamScroll(ABC): # where every class inherits from
    def __init__(self, camera, player):
        self.camera = camera
        self.player = player
    
    @abstractmethod # if spot isn't filled Python will know something
    # went wrong
    def scroll(self):
        pass

class Follow(CamScroll):
    def __init__(self, camera, player):
        CamScroll.__init__(self, camera, player)
    
    def scroll(self): # updates camera's postion based on player's current position
        # adds the difference onto the camera's positon
        # self.CONST allows you to control the camera is focused
        # if self.CONST is half the screen - offset player will appear center
        # adding the const on to the offset is what will center the player
        self.camera.offset_float.x += (self.player.pos.x - self.camera.offset_float.x + self.camera.CONST.x)
        self.camera.offset_float.y += (self.player.pos.y - self.camera.offset_float.y + self.camera.CONST.y)
        self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)

class Border(CamScroll): # prevents cam from scrolling off completely
    def __init__(self, camera, player):
        CamScroll.__init__(self, camera, player)
    
    def scroll(self): 
        self.camera.offset_float.x += (self.player.pos.x - self.camera.offset_float.x + self.camera.CONST.x)
        self.camera.offset_float.y += (self.player.pos.y - self.camera.offset_float.y + self.camera.CONST.y)
        self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)
        self.camera.offset.x = max(self.player.left_border, self.camera.offset.x)
        self.camera.offset.x = min(self.camera.offset.x, self.player.right_border - self.camera.DISPLAY_W)

class Auto(CamScroll): # camera moves independently of player
    def __init__(self, camera, player):
        CamScroll.__init__(self, camera, player)
    
    def scroll(self):
        self.camera.offset.x += 1
