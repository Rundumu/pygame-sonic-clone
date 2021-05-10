import pygame
from settings import *

vec = pygame.math.Vector2

class Sonic(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 51)
        self.pos = vec(WIDTH / 2 , HEIGHT - 51)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.last_update = 0
        self.time_passed = 0
        

    def update(self):
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
            self.time_passed += (now - self.last_update)
            self.acc.x /= 0.5 # player becomes 50% faster
            if self.time_passed >= 3000:
                self.acc.x /= 0.75

# environment classes          
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

class Ramp(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, width, height)
        self.height = height
        self.width = width
        self.rect.x = x
        self.rect.y = y
        self.x1, self.y1 = self.rect.bottomleft
        self.x2, self.y2 = self.rect.topright
        self.x3, self.y3 = self.rect.bottomright
        self.image = pygame.draw.polygon(window, GREEN, [[self.x1, self.y1], 
                                        [self.x2, self.y2], [self.x2, self.y3]])
    
    # TODO: Figure out a way to create a function that creates ramps and collision

    # def update(self):
    #     pygame.draw.polygon(window, GREEN, [[self.x1, self.y1], 
    #     [self.x2, self.y2], [self.x2, self.y3]])

# creates a camera that follows the player
class Camera():
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
    
    # set the camera's focus - offset then applied to above Rect
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft) # move by current camera's (0, 0) and returns a new rect
    
    # update the camera's position
    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2) # keeps player centered
        y = -target.rect.y + int(HEIGHT - 50) # keeps player centered
 
        x = min(0, x) # ensure camera doesn't go off the screen
        y = min(0, y)

        self.camera = pygame.Rect(x, y, self.width, self.height)
