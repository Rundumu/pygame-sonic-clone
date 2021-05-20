from settings import *
from sprites import *
from os import path
import pygame
import math


pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
running = True

current_dir = path.dirname(__file__)
maps_dir = path.join(current_dir, 'maps')

# def create_ramp(x, y, width, height):
#     hitbox = pygame.draw.rect(window, BLUE, [x, y, width, height])
#     x1, y1 = hitbox.bottomleft
#     x2, y2 = hitbox.topright
#     x3, y3 = hitbox.bottomright
#     ramp = pygame.draw.polygon(window, GREEN, [[x1, y1], 
#                                         [x2, y2], [x3, y3]])

# initialise camera
camera = Camera(WIDTH, HEIGHT)


# player sprites
s = Sonic()
player = pygame.sprite.Group()

# floor sprites
ground = Ground(0, HEIGHT - 50, GROUND)
floor = pygame.sprite.Group()
floor.add(ground)


# with open(path.join(maps_dir, 'plats.txt'), 'r') as f:
#     data = f.readlines()

#     for line in data:
#         p = Platform(int(data[0]), int(data[0]), SMALL)
#         plats.add(p)
#         platforms.append(p)
    
# ramps
X1 = 200
Y1 = HEIGHT- 50

X2 = 120
Y2 = HEIGHT - 50

X3 = 200
Y3 = HEIGHT - 200    

ramp = Ramp(940, HEIGHT - 50, 160, 160)
ramp2 = Ramp(2500, HEIGHT - 50, 300, 300)
ramps = pygame.sprite.Group()
ramps.add(ramp)
ramps.add(ramp2)

# spikes
spike = Spike(550, HEIGHT - 65)
spikes = pygame.sprite.Group()
spikes.add(spike)

# loops
# loop = Loop(2000, HEIGHT - 50)
# loops = pygame.sprite.Group()
# loops.add(loop)

# enemies
enemy = Enemies(1200, HEIGHT - 100)
enemies = pygame.sprite.Group()
enemies.add(enemy)

# all sprites
sprites = pygame.sprite.Group()
sprites.add(s)
sprites.add(ground)
sprites.add(ramp)
sprites.add(ramp2)       
sprites.add(spike)
sprites.add(enemy)
#sprites.add(loop)

# rings
# ring = Ring(100, HEIGHT - 120)
# ring_x_offset = 50
# ring_y = HEIGHT - 120

# ring_x_distance = 500
rings = pygame.sprite.Group()


# for i in range(150):
#     ring_x_offset += 50
#     print(ring_x_offset)
#     ring = Ring(ring_x_offset, ring_y)
#     rings.add(ring)
#     if ring_x_offset > 150:
#         ring = Ring(ring_x_distance, ring_y)
#         rings.add(ring)

for ring in RING_LIST:
    r = Ring(*ring)
    rings.add(r)
    sprites.add(r)       

# platform sprites
plats = pygame.sprite.Group()

for p in PLATFORM_LIST:
    plat = Platform(*p)
    plats.add(plat)
    sprites.add(plat)


# TODO: figure out a way to blit the camera (done)

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update
    #ramps.update()
    rings.update()
    enemy.update()
    spikes.update()
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



    hits = pygame.sprite.spritecollide(s, plats, False)

    if hits:
        for hit in hits:
            if abs(s.pos.x - hit.rect.left) < 10 and s.vel.x > 0:
                print(hit.rect.x)
                s.pos.x = (hit.rect.left - 1)
                s.pos.x = s.rect.left
                s.vel.x = 0  
            if abs(s.pos.x - hit.rect.right) < 10 and s.vel.x < 0:
                print(hit.rect.x)
                s.rect.left = (hit.rect.right + 50)
                s.pos.x = s.rect.left
                s.vel.x = 0
            if abs(s.pos.y - hit.rect.top) < 10 and s.vel.y > 0:
                print(hit.rect.x)
                s.pos.y = hit.rect.top
                s.rect.bottom = s.pos.y
                s.vel.y = 0
            if abs(s.rect.top - hit.rect.bottom) < 10 and s.vel.y < 0:
                print(hit.rect.x)
                s.rect.top = (hit.rect.bottom + 1) 
                s.pos.y = s.rect.bottom
                s.vel.y = 0
        
    ramp_hits = pygame.sprite.spritecollide(s, ramps, False)

    if ramp_hits:
        for hit in ramp_hits:
            rel_x = s.pos.x - hit.rect.x

            pos_height = rel_x + s.rect.width

            pos_height = min(pos_height, ramp_hits[0].rect.height)
            pos_height = max(pos_height, 0)

            target_y = ramp_hits[0].rect.y + ramp_hits[0].rect.height - pos_height

            if s.rect.bottom > target_y:
                s.rect.bottom = target_y
                s.pos.y = s.rect.bottom

    ring_hits = pygame.sprite.spritecollide(s, rings, False)

    if ring_hits:
        RING_COUNT += 1
        print(RING_COUNT)
        ring_hits[0].kill()

    pricks = pygame.sprite.spritecollide(s, spikes, False)

    if pricks:
        for prick in pricks:
            if s.vel.y > 0 and s.rect.bottom > prick.rect.top:
                s.rect.bottom = prick.rect.top
                s.pos.y = s.rect.bottom
                s.pos.x = (prick.rect.left - 50)
                s.vel.y = 0
                s.vel.x = 0
                RING_COUNT = 0
                print(RING_COUNT)
            if s.vel.x > 0 and s.rect.right > prick.rect.left:
                s.rect.right = (prick.rect.left - 50)
                s.pos.x = s.rect.right
                s.vel.x = 0
                s.vel.y = 0
            if s.vel.x < 0 and s.rect.left < prick.rect.right:
                s.rect.left = (prick.rect.right + 50)
                s.pos.x = s.rect.left
                s.vel.x = 0
                s.vel.y = 0



    # TODO: create an exploding list that generates rings (done)
    
    clashes = pygame.sprite.spritecollide(s, enemies, False)

    if clashes:
        for clash in clashes:
            if s.vel.y > 0 and s.rect.bottom > clash.rect.top and s.rect.bottom != ground.rect.top:
                s.vel.y = 0
                clash.vel = 0
                s.rect.bottom = clash.rect.top
                s.pos.y = s.rect.bottom
                clash.kill()

            if abs(s.rect.left - clash.rect.right) < 10:
                s.rect.left = (clash.rect.right + 50)
                s.pos.x = s.rect.left
                clash.vel = (clash.vel * -1)
                RING_COUNT = 0 
                # TODO: study collisions with moving objects
                print(RING_COUNT)
            
            if abs(s.rect.right - clash.rect.left) < 10:
                s.rect.right = (clash.rect.left - 50)
                s.pos.x = s.rect.right
                clash.vel = (clash.vel * -1)
                RING_COUNT = 0 
                # TODO: study collisions with moving objects
                print(RING_COUNT)
        
    camera.update(s)


    # draw
    window.fill(BLACK)
    
    for sprite in sprites:
        window.blit(sprite.image, camera.apply(sprite))

    

#TODO: Create a way to dynamically generate platforms

    # double buffering 
    pygame.display.flip()
