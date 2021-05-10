from settings import *
from sprites import *
import pygame

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
running = True



# initialise camera
camera = Camera(WIDTH, HEIGHT)


# player sprites
s = Sonic()
player = pygame.sprite.Group()

# floor sprites
ground = Ground(0, HEIGHT - 50, GROUND)
floor = pygame.sprite.Group()
floor.add(ground)

# platform sprites

platforms = [Platform(WIDTH + 200, HEIGHT - 300, SMALL)]

plats = pygame.sprite.Group()

platx = 100 

platy = 50

collision_threshold = 1

for i in platforms:
    plats.add(i)


# ramps
X1 = 200
Y1 = HEIGHT- 50

X2 = 120
Y2 = HEIGHT - 50

X3 = 200
Y3 = HEIGHT - 200    

ramp = Ramp(200, HEIGHT - 150, 100, 100)



# all sprites
sprites = pygame.sprite.Group()
sprites.add(s)
sprites.add(plats)
sprites.add(ground)
sprites.add(ramp)         
            

# TODO: figure out a way to blit the camera (done)

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update
    
    sprites.update()


    if s.vel.y > 0:
        collisions = pygame.sprite.spritecollide(s, floor, False)

        if collisions:
            for collision in collisions:
                # TODO: create different classes of platforms each with their own collision properties (done)
                if s.pos.y > collision.rect.top: 
                    s.pos.y = collision.rect.top
                    s.rect.bottom = s.pos.y
                    s.vel.y = 0 

    # if s.vel.x > 0:
    #     hits = pygame.sprite.spritecollide(s, plats, False)

    #     if hits:
    #         for hit in hits:
    #             if abs(s.rect.right - hit.rect.left) < 10:
    #                 s.pos.x = (hit.rect.left - 1) 
    #                 s.rect.right = s.pos.x
    #                 s.vel.x = 0

    # if s.vel.x < 0:
    #     hits = pygame.sprite.spritecollide(s, plats, False)

    #     if hits:
    #         for hit in hits:
    #             if abs(s.rect.left - hit.rect.right) < 10:
    #                 s.pos.x = (hit.rect.right + 1)
    #                 s.rect.left = s.pos.x
    #                 s.vel.x = 0

    # if s.vel.y > 0:
    #     hits = pygame.sprite.spritecollide(s, plats, False)

    #     if hits:
    #         for hit in hits:
    #             if abs(s.rect.bottom - hit.rect.top) < 10:
    #                 print('collision')
    #                 s.pos.y = (hit.rect.top + 1)
    #                 s.rect.bottom = s.pos.y
    #                 s.vel.y = 0

    hits = pygame.sprite.spritecollide(s, plats, False)

    if hits:
        for hit in hits:
            if abs(s.pos.x - hit.rect.left) < 10 and s.vel.x > 0:
                s.pos.x = (hit.rect.left - 1)
                s.pos.x = s.rect.left
                s.vel.x = 0  
            if abs(s.rect.left - hit.rect.right) < 10 and s.vel.x > 0:
                print(s.vel)
                s.rect.left = (hit.rect.right + 1)
                s.pos.x = s.rect.right
                s.vel.x = 0
            if abs(s.pos.y - hit.rect.top) < 10 and s.vel.y > 0:
                s.pos.y = hit.rect.top  
                s.rect.bottom = s.pos.y
                s.vel.y = 0
            if abs(s.rect.top - hit.rect.bottom) < 10 and s.vel.y < 0:
                s.rect.top = (hit.rect.bottom + 1) 
                s.pos.y = s.rect.bottom
                s.vel.y = 0
    
    
        
    camera.update(s)

    # draw
    window.fill(BLACK)
    
    for sprite in sprites:
        window.blit(sprite.image, camera.apply(sprite))
        
    
    #ramp.ramp()

    

#TODO: Create a way to dynamically generate platforms

    # double buffering 
    pygame.display.flip()
