from settings import *
from sprites import *
from camera import *
import pygame

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
running = True


window = pygame.display.set_mode((WIDTH, HEIGHT))



# player sprites
s = Sonic()

# floor sprites
ground = Ground(0, HEIGHT - 50, GROUND)
floor = pygame.sprite.Group()
floor.add(ground)

# platform sprites
plat1 = Platform(WIDTH - 100, HEIGHT - 100, SMALL)
plat2 = Platform(WIDTH - 100, HEIGHT - 150, SMALL)
plats = pygame.sprite.Group()
plats.add(plat1)
plats.add(plat2)


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
                    s.pos.y = collision.rect.top
                    s.vel.y = 0

    for plat in plats.sprites():
        if s.rect.colliderect(plat) and s.pos.x > plat.rect.left and not s.rect.y < plat.rect.top:
            s.pos.x = plat.rect.left - 1 # player sprite will be scaled down by 25px
            s.vel.x = 0
        if s.rect.colliderect(plat) and s.pos.y > plat.rect.top and not s.rect.x < plat.rect.left:
            s.pos.y = plat.rect.top
            s.vel.y = 0
    
        
    # if s.pos.x > WIDTH:
    #     for plat in plats.sprites():
    #         plat.rect.x -= max(abs(s.vel.x), 2)
    #         # set locations for each platform
    #         # set the camera to follow sonic so that he doesn't disappear off the screen
    #         print("poop")

    
    sprites.update()
    plats.update()

    #camera.scroll()

    # draw
    window.fill(BLACK)
    
    for plat in plats:
        window.blit(plat.image, (s.pos.x + SCROLL[0], s.pos.y + SCROLL[1]))
    
    floor.draw(window)
    

#TODO: Create a map file for the game

    # double buffering 
    pygame.display.flip()
