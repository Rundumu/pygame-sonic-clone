from settings import *
from sprites import *
import pygame

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
running = True


window = pygame.display.set_mode((WIDTH, HEIGHT))

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

platforms = [Platform(WIDTH + 200, HEIGHT - 100, SMALL)]

plats = pygame.sprite.Group()

platx = 100 

platy = 50

collision_threshold = 1

for i in platforms:
    plats.add(i)
    

# all sprites
sprites = pygame.sprite.Group()
sprites.add(s)
sprites.add(plats)
sprites.add(ground)         
            

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
        if abs(s.pos.x - hits[0].rect.left) < 10 and s.vel.x > 0:
            s.pos.x = (hits[0].rect.left - 1)
            s.pos.x = s.rect.left
            s.vel.x = 0  
        if abs(s.rect.left - hits[0].rect.right) < 10 and s.vel.x < 0:
            print('collision')
            s.rect.left = (hits[0].rect.right + 1)  
            s.pos.x = s.rect.left
            s.vel.x = 0
    if hits:
        if abs(s.pos.y - hits[0].rect.top) < 10 and s.vel.y > 0:
            s.pos.y = hits[0].rect.top  
            print(hits[0].rect.top)
            s.rect.bottom = s.pos.y
            s.vel.y = 0
        if abs(s.rect.top - hits[0].rect.bottom) < 10 and s.vel.y < 0:
            s.rect.top = (hits[0].rect.bottom + 1) 
            s.pos.y = s.rect.bottom
            s.vel.y = 0
        
    camera.update(s)

    # draw
    window.fill(BLACK)
    
    for sprite in sprites:
        window.blit(sprite.image, camera.apply(sprite))
    
    

#TODO: Create a way to dynamically generate platforms

    # double buffering 
    pygame.display.flip()
