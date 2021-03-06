import pygame
from settings import *
from spritesheet import Spritesheet
import math
import time

vec = pygame.math.Vector2
            
class Sonic(pygame.sprite.Sprite):
    
    def __init__(self, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.spritesheet = Spritesheet("spritesheet.png")
        self.image = self.spritesheet.get_sprite(0, 0, 234, 252)
        self.image.set_colorkey(CYAN)
        self.image = pygame.transform.scale(self.image, (100, 100))
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 41)
        self.pos = vec(WIDTH / 4 , HEIGHT - 10)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.jumping = False
        self.standing = True
        self.last_update = 0
        self.time_passed = 0
        self.current_frame = 0
        self.left_current_frame = 0
        self.standing_frames = 0
        self.jumping_frames = 0
        self.previous_frame = 0
        self.previous_standing_frame = 0
        self.animating = False
        self.radians = 0
        self.circ_vel = -20
        

    def stand(self):
        if self.standing:
            self.spritesheet = Spritesheet("spritesheet.png")
            self.image = self.spritesheet.get_sprite(0, 0, 234, 252)
            self.image.set_colorkey(CYAN) 
            self.image = pygame.transform.scale(self.image, (100, 100))

            
            
            if self.standing_frames < len(self.game.s_standing):
                self.standing_frames += 0.01
                if self.standing_frames >= len(self.game.s_standing):
                    self.standing_frames = 0
                self.image = self.game.s_standing[int(self.standing_frames)]
                self.image.set_colorkey(CYAN) 
                self.image = pygame.transform.scale(self.image, (100, 100))
            
            
        

    def jump(self):
        try:
            if self.jumping:
                self.spritesheet = Spritesheet("spritesheet3.png")
                self.image = self.spritesheet.get_sprite(0, 0, 232, 252)
                self.image.set_colorkey(CYAN) 
                self.image = pygame.transform.scale(self.image, (100, 100))

                    
                now = pygame.time.get_ticks()
                self.jumping_frames += 0.001
                                        
                                    
                self.jumping_frames = (self.jumping_frames + 1) % len(self.game.s_jumping)        
                self.image = self.game.s_jumping[int(self.jumping_frames)]
                self.image.set_colorkey(CYAN) 
                self.image = pygame.transform.scale(self.image, (100, 100))
                
            self.rect.y += 1
            hits = pygame.sprite.spritecollide(self, self.game.floor, False)
            self.rect.y -= 1

            self.rect.y += 1
            hitting = pygame.sprite.spritecollide(self, self.game.plats, False)
            self.rect.y -= 1

            if hitting or not self.jumping:
                self.jumping = True
                self.vel.y -= PLAYER_JUMP

            if hits or not self.jumping:
                print(hits)
                self.jumping = True
                self.vel.y -= PLAYER_JUMP
        except IndexError:
            pass



        
    # def limit_jump(self):
    #     if self.jumping:
    #         if self.vel.y < -3:
    #             self.vel.y = -3

    def update(self, dt):
        self.acc = vec(0, GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -ACCEL - 2
            self.faster()
            self.runLeft()
        if keys[pygame.K_RIGHT]:
            self.animate()
            self.runRight()
            self.acc.x = ACCEL
            self.faster()
        if keys[pygame.K_SPACE]:
            self.jump()
        else:
            if 1 not in keys:
                self.stand()
        # if self.jumping == False and keys[pygame.K_SPACE]:
        #     self.acc.y = -ACCEL
        #     self.jumping = True
        # if self.jumping == True:
        #     if self.vel.y < -3:
        #         self.vel.y = -3
        #         self.jumping = False
        

                
        # if keys[pygame.K_DOWN]:
        #     self.radians += self.circ_vel
        #     self.acc.x = self.acc.x + math.cos(self.radians) * -50
        #     self.acc.y = self.acc.y + math.sin(self.radians) * -50
        #     print(math.cos(self.radians))

        
                       
                       
                        
        # jumping animations
             
       
       # friction check
        self.acc.x += self.vel.x * FRICTION
        if self.vel.x < -2:
            self.vel.x = -2

       # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # if self.pos.x > WIDTH:
        #     self.pos.x = 0
        if self.pos.x < 0:
            self.rect.left = 0
            self.pos.x = self.rect.left

        self.rect.midbottom = self.pos

    # sonic speed feature - get faster after running for x amount of time
    def faster(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > FASTER_TIME:
            self.time_passed += (now - self.last_update)
            self.acc.x /= 0.5 # player becomes 50% faster
            if self.time_passed >= 3000:
                self.acc.x /= 0.75
    
    def animate(self):
        self.animating = True
    
    

    def runLeft(self):
            self.spritesheet = Spritesheet("spritesheet2.png")
            self.image = self.spritesheet.get_sprite(0, 0, 234, 252)
            self.image = pygame.transform.smoothscale(self.image, (50, 50))            
            
            self.left_current_frame += 0.01


            if self.animating == True:
                self.left_current_frame = (self.left_current_frame + 1) % len(self.game.s_running)

                self.image = self.game.s_running[int(self.left_current_frame)]
                self.image = pygame.transform.smoothscale(self.image, (100, 100))
                self.image = pygame.transform.flip(self.image, True, False)
                self.image.set_colorkey(CYAN)

                # self.sprite.set_colorkey(CYAN)
                # self.image.set_colorkey(CYAN)

    def runRight(self):
            self.spritesheet = Spritesheet("spritesheet2.png")
            self.image = self.spritesheet.get_sprite(0, 0, 234, 252)
            self.image = pygame.transform.smoothscale(self.image, (100, 100))    
            
            if self.current_frame < len(self.game.s_running):
                self.current_frame += 0.1

                if self.current_frame > len(self.game.s_running):
                    self.current_frame = 0

                self.image = self.game.s_running[int(self.current_frame)]
                self.image = pygame.transform.smoothscale(self.image, (100, 100))
                self.image.set_colorkey(CYAN)

class Background(pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("background.png").convert()
        self.image = pygame.transform.smoothscale(self.image, (width, height))
        # self.image.fill(layer)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width

    def update(self, dt):
        pass

# environment classes          
class Ground(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((GROUND))
        self.image.fill(GREEN)
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self, dt):
        pass


class Platform(pygame.sprite.Sprite):

    def __init__(self, game, x, y, plat):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((plat))
        self.image = pygame.image.load("platform.png")
        self.image = pygame.transform.scale(self.image, (plat))
        # self.image.fill(GREEN)
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, dt):
        pass
    
class Ramp(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, ramp=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.ramp = ramp
        self.x1, self.y1 = self.rect.bottomleft
        self.x2, self.y2 = self.rect.topright
        self.x3, self.y3 = self.rect.bottomright
        


    # TODO: Figure out a way to create a function that creates ramps and collision

    def update(self, dt):
        if self.ramp == 1:
            self.image = pygame.image.load("ramp1.png").convert_alpha()
            self.image.set_colorkey(PLATFORM_BLUE)
        if self.ramp == 2:
            self.image = pygame.image.load("ramp2.png")
            self.image.set_colorkey(PLATFORM_BLUE)


class Ring(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((15, 15))
        self.image = pygame.image.load("ring.png")
        self.image = pygame.transform.scale(self.image, (15, 15))
        #self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.ring_frames = 0
        self.rect.x = x
        self.rect.y = y
    
    def update(self, dt):
        pass
        # self.spritesheet = Spritesheet("spritesheet4.png")
        # self.image = self.spritesheet.get_sprite(0, 0, 234, 252)
        # self.image = pygame.transform.scale(self.image, (50, 50))
        
        # if self.ring_frames < len(self.game.ring_images):
        #     self.ring_frames += 2

        #     if self.ring_frames >= len(self.game.ring_images):
        #         self.ring_frames = 0

        #     self.image = self.game.ring_images[int(self.ring_frames)]
        #     self.image = pygame.transform.scale(self.image, (50, 50))
        #     self.image.set_colorkey(CYAN)

class Spike(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((30, 50))
        self.image = pygame.image.load("spike.png").convert()
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (30, 50))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

    
    def update(self, dt):
        pass

class Enemies(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((50, 50))
        # self.image.fill(RED)
        self.spritesheet = Spritesheet("spritesheet5.png")
        self.image = self.spritesheet.get_sprite(0, 0, 234, 252)
        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.smoothscale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.current_frame = 0
        self.vel = 2
        self.start = (x - 100)
        self.end = (x + 100)
        self.path = [self.start, self.end]

    def update(self, dt):
        self.animate()
        if self.vel > 0:
            if self.rect.x + self.vel < self.path[1]:
                self.rect.x += self.vel 
            else:
                self.vel = (self.vel * -1) 
        else:
            if self.rect.x - self.vel > self.path[0]:
                self.rect.x += self.vel 
            else:
                self.vel = (self.vel * -1)

    def animate(self):
        for i in self.game.enemy_images:
            self.current_frame += 0.01
            if self.current_frame < len(self.game.enemy_images):
                self.image = self.game.enemy_images[int(self.current_frame)]
                self.image.set_colorkey(KINDA_WHITE)
                self.image = pygame.transform.scale(self.image, (50, 50))

            if self.current_frame >= len(self.game.enemy_images):
                self.current_frame = 0                




# class Loop(pygame.sprite.Sprite):

#     def __init__(self, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((200, 200))
#         self.image.fill(GREEN)
#         self.rect = self.image.get_rect()
#         self.rect.midbottom = (x, y)

#     def update(self):
#         pass

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




