import pygame
from settings import *
from camera import *

vec = pygame.math.Vector2

class Sonic(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2 , HEIGHT - 51)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.last_update = 0
        

    def update(self):
        #camera = Camera(self)
        self.acc = vec(0, GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -ACCEL - 2
            self.faster()
        if keys[pygame.K_RIGHT]:
            self.acc.x = ACCEL
            self.faster()
        if keys[pygame.K_UP]:
            self.acc.y = -ACCEL
                    
       
       # friction check
        self.acc.x += self.vel.x * FRICTION
        if self.vel.x < -2:
            self.vel.x = -2

       # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # if self.pos.x > WIDTH:
        #     self.pos.x = 0
        # if self.pos.x < 0:
        #     self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    # sonic speed feature - get faster after running for x amount of time
    def faster(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > FASTER_TIME:
            self.acc.x /= 0.5 # player becomes 50% faster
            if self.vel.x == 0: # if player's velocity is 0 then the player 
                self.acc.x -= 0.5

class Ground(pygame.sprite.Sprite):

    def __init__(self, x, y, plat):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((GROUND))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        


class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, plat):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((plat))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# # creates a camera that follows the player
# class Camera():
#     def __init__(self, camera_func, width, height):
#         self.camera_func = camera_func
#         self.state = pygame.Rect(0, 0, width, height)
    
#     # set the camera's focus
#     def apply(self, target):
#         return target.rect.move(self.state.topleft)
    
#     # update the camera's position
#     def update(self, target):
#         self.state = self.camera_func(self.state, target.rect)