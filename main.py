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
    if s.vel.y > 0:
        collisions = pygame.sprite.spritecollide(s, floor, False)

        if collisions:
            for collision in collisions:
                # TODO: create different classes of platforms each with their own collision properties (done)
                if s.pos.y > collision.rect.top: 
                    s.vel.y = (s.vel.y - 0.6)
                    s.pos.y = collision.rect.top
                    
                
    
    # TODO: figure out how to reset x vel when jumping
    
    if s.vel.x > 0:
        hits = pygame.sprite.spritecollide(s, plats, False)
        
        if hits:
            for hit in hits:
                if s.pos.x > hit.rect.left and s.pos.x < hit.rect.right:
                    s.vel.x = 0
                    s.pos.x = (hit.rect.left - 30)
                    
    if s.vel.x < 0:
        hits = pygame.sprite.spritecollide(s, plats, False)

        if hits:
            for hit in hits:
                if s.pos.x < hit.rect.right and s.pos.x > hit.rect.left:
                    s.vel.x = 0
                    s.pos.x = (hit.rect.right + 30)
    
    if s.vel.y > 0:
        s.vel.x = 0
        s.vel.y = 0
        hits = pygame.sprite.spritecollide(s, plats, False)

        if hits:
            for hit in hits:
                if s.pos.y > hit.rect.top:
                    s.vel.y = 0
                    s.pos.y = hit.rect.top
    
    if s.vel.y < 0:
        if s.vel.x > 0 and s.vel.x < 0:
            s.vel.x = 0
        hits = pygame.sprite.spritecollide(s, plats, False)

        if hits:
            for hit in hits:
                if s.pos.y < hit.rect.bottom:
                    s.vel.x = 0
                    s.vel.y = 0
                    s.pos.y = hit.rect.bottom
    


                
                # if s.vel.x < 0:
                #     s.rect.left = hits[0].rect.right
                #     s.vel.x = 0
                # if s.vel.y < 0:
                #     s.rect.top = hits[0].rect.bottom
                #     s.vel.y = 0
                # if s.vel.y > 0:
                #     s.rect.bottom = hits[0].rect.top
                #     s.vel.y = 0
            

    
        
    # if s.pos.x > WIDTH:
    #     for plat in plats.sprites():
    #         plat.rect.x -= max(abs(s.vel.x), 2)
    #         # set locations for each platform
    #         # set the camera to follow sonic so that he doesn't disappear off the screen
    #         print("poop")

    print(s.vel)
    
    sprites.update()
    camera.update(s)

    # draw
    window.fill(BLACK)
    
    for sprite in sprites:
        window.blit(sprite.image, camera.apply(sprite))
    
    

#TODO: Create a way to dynamically generate platforms

    # double buffering 
    pygame.display.flip()
