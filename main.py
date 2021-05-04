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

platforms = [Platform(WIDTH + 200, HEIGHT - 300, SMALL)]

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

def plat_collision_y():
    hits = pygame.sprite.spritecollide(s, plats, False)
    
    if s.vel.y > 0:
        if hits:
            # s.vel.x = int(s.vel.x)

            # s.vel.y = int(s.vel.y)
            
            # print(s.vel)
            for hit in hits:
                if s.pos.y > hit.rect.top:
                    s.pos.y = hit.rect.top
                    s.rect.bottom = s.pos.y
                    s.vel.y = 0

def plat_collision_x():
    cols = pygame.sprite.spritecollide(s, plats, False)
    
    if s.vel.x > 0:
        if cols:
            # s.vel.x = int(s.vel.x)

            # s.vel.y = int(s.vel.y)
            
            # print(s.vel)
            for hit in hits:
                if s.pos.x > hit.rect.left:
                    s.pos.x = hit.rect.left
                    s.rect.right = s.pos.x
                    s.vel.y = 0


    
    
        
                
        
        # elif hits[0].rect.right > s.rect.left:
        #     s.vel.x = 0
        #     s.pos.x = hits[0].rect.right
        #     s.rect.left = s.pos.x
            
            

        # elif hits[0].rect.left < s.rect.right:
        #     s.vel.x = 0
        #     s.pos.x = hits[0].rect.left
        #     s.rect.right = s.pos.x
            
            

    


# TODO: figure out a way to blit the camera (done)

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update

    

    sprites.update()
    # print(s.vel)

    plat_collision_y()
    plat_collision_x()


    if s.vel.y > 0:
        collisions = pygame.sprite.spritecollide(s, floor, False)

        if collisions:
            for collision in collisions:
                # TODO: create different classes of platforms each with their own collision properties (done)
                if s.pos.y > collision.rect.top: 
                    s.pos.y = collision.rect.top
                    s.rect.bottom = s.pos.y
                    s.vel.y = 0 
                    # print(s.acc)
                    # print(s.vel)
                    
    
    

                # if s.pos.y < hit.rect.bottom:
                #     s.pos.y = hit.rect.bottom
                #     s.rect.bottom = s.pos.y
                #     # print(s.acc)
                #     # print(s.vel)


                
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

    
    

    camera.update(s)

    # draw
    window.fill(BLACK)
    
    for sprite in sprites:
        window.blit(sprite.image, camera.apply(sprite))
    
    

#TODO: Create a way to dynamically generate platforms

    # double buffering 
    pygame.display.flip()
