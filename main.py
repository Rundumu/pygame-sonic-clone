from pygame.sprite import Sprite
from settings import *
from sprites import *
from spritesheet import Spritesheet
from os import path
import pygame


class Game():
    
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.running = True
        self.clock = pygame.time.Clock()
        self.camera = Camera(WIDTH, HEIGHT)
        self.ring_count = 0
        self.window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    
    def new_game(self):

        self.s_run = Spritesheet('spritesheet2.png')
        self.s_running = [self.s_run.parse_sprite("sonic-run1.png"), 
                        self.s_run.parse_sprite("sonic-run2.png"),
                        self.s_run.parse_sprite("sonic-run3.png"),
                        self.s_run.parse_sprite("sonic-run4.png"),
                        self.s_run.parse_sprite("sonic-run5.png")]
        
        self.s_stand = Spritesheet('spritesheet.png')
        self.s_standing = [self.s_stand.parse_sprite("sonic1.png"), 
                        self.s_stand.parse_sprite("sonic2.png"),
                        self.s_stand.parse_sprite("sonic3.png"),
                        self.s_stand.parse_sprite("sonic4.png")] 

        self.s_jump = Spritesheet('spritesheet3.png')
        self.s_jumping = [self.s_jump.parse_sprite("sonic-jump1.png"), 
                        self.s_jump.parse_sprite("sonic-jump2.png"),
                        self.s_jump.parse_sprite("sonic-jump3.png"),
                        self.s_jump.parse_sprite("sonic-jump4.png"),
                        self.s_jump.parse_sprite("sonic-jump5.png"),
                        self.s_jump.parse_sprite("sonic-jump6.png"),
                        self.s_jump.parse_sprite("sonic-jump7.png")]
        
        # self.ring_img = Spritesheet("spritesheet4.png")
        # self.ring_images = [self.ring_img.parse_sprite("ring1.png"), 
        #                 self.ring_img.parse_sprite("ring2.png"),
        #                 self.ring_img.parse_sprite("ring3.png"),
        #                 self.ring_img.parse_sprite("ring4.png"),
        #                 self.ring_img.parse_sprite("ring5.png"),
        #                 self.ring_img.parse_sprite("ring6.png"),
        #                 self.ring_img.parse_sprite("ring7.png"),
        #                 self.ring_img.parse_sprite("ring8.png"),
        #                 self.ring_img.parse_sprite("ring9.png")]
        
        self.enemy_img = Spritesheet('spritesheet5.png')
        self.enemy_images = [self.enemy_img.parse_sprite("enemy1.png"), 
                        self.enemy_img.parse_sprite("enemy2.png"),
                        self.enemy_img.parse_sprite("enemy3.png"),
                        self.enemy_img.parse_sprite("enemy4.png"),
                        self.enemy_img.parse_sprite("enemy5.png"),
                        self.enemy_img.parse_sprite("enemy6.png"),
                        self.enemy_img.parse_sprite("enemy7.png")]               

        # groups
        self.sprites = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()
        self.rings = pygame.sprite.Group()
        self.ramps = pygame.sprite.Group()
        self.plats = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # sprites   
        self.s = Sonic(self)
        self.ground = Ground(self, 0, HEIGHT - 50)

        # adding to groups
        
        self.sprites.add(self.s)
        self.sprites.add(self.ground)
        self.floor.add(self.ground)

        # procedural generation (not sure)
        for ring in RING_LIST:
            r = Ring(self, *ring)
            self.rings.add(r)
            self.sprites.add(r) 

        for r in RAMP_LIST:
            r = Ramp(*r)
            self.ramps.add(r)
            self.sprites.add(r)

        for p in PLATFORM_LIST:
            plat = Platform(self, *p)
            self.plats.add(plat)
            self.sprites.add(plat)

        for i in SPIKE_LIST:
            spike = Spike(*i)
            self.spikes.add(spike)
            self.sprites.add(spike)

        for e in ENEMY_LIST:
            enemy = Enemies(*e)
            self.enemies.add(enemy)
            self.sprites.add(enemy)
        
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            print(self.dt)
            self.events()
            self.update(self.dt)
            self.draw()

    def draw(self):
        # draw
        self.window.fill(BLACK)
        
        for sprite in self.sprites:
            self.window.blit(sprite.image, self.camera.apply(sprite))

        pygame.display.flip()

    def update(self, dt):
        # update

        # self.rings.update()
        # self.enemy.update()
        # self.spikes.update()
        self.sprites.update(dt)


        if self.s.vel.y > 0:
            collisions = pygame.sprite.spritecollide(self.s, self.floor, False)

            if collisions:
                for collision in collisions:
                    # TODO: create different classes of platforms each with their own collision properties (done)
                    if self.s.pos.y > collision.rect.top: 
                        self.s.pos.y = collision.rect.top
                        self.s.rect.bottom = self.s.pos.y
                        self.s.vel.y = 0 



        hits = pygame.sprite.spritecollide(self.s, self.plats, False)

        if hits:
            for hit in hits:
                if abs(self.s.pos.x - hit.rect.left) < 10 and self.s.vel.x > 0:
                    self.s.pos.x = (hit.rect.left - 1)
                    self.s.pos.x = self.s.rect.left
                    self.s.vel.x = 0  
                if abs(self.s.pos.x - hit.rect.right) < 10 and self.s.vel.x < 0:
                    self.s.rect.left = (hit.rect.right + 1)
                    self.s.pos.x = self.s.rect.left
                    self.s.vel.x = 0
                if abs(self.s.pos.y - hit.rect.top) < 10 and self.s.vel.y > 0:
                    self.s.pos.y = hit.rect.top
                    self.s.rect.bottom = self.s.pos.y
                    self.s.vel.y = 0
                if abs(self.s.rect.top - hit.rect.bottom) < 10 and self.s.vel.y < 0:
                    self.s.rect.top = (hit.rect.bottom + 1) 
                    self.s.pos.y = self.s.rect.bottom
                    self.s.vel.y = 0
            
        ramp_hits = pygame.sprite.spritecollide(self.s, self.ramps, False)

        if ramp_hits:
            for hit in ramp_hits:
                rel_x = self.s.pos.x - hit.rect.x

                if hit.ramp == 1:
                    pos_height = rel_x + self.s.rect.width
                    pos_height = min(pos_height, ramp_hits[0].rect.height)
                    pos_height = max(pos_height, 0)               
                elif hit.ramp == 2:
                    pos_height = hit.rect.width - rel_x
                    pos_height = min(pos_height, ramp_hits[0].rect.height)
                    pos_height = max(pos_height, 0)
                if hit.ramp == 2 and abs(self.s.rect.right - hit.rect.left) < 10 and self.s.vel.x > 0:
                    self.s.rect.right = hit.rect.left
                    self.s.pos.x = hit.rect.left
                    self.s.vel.x = 0

                pos_height = min(pos_height, ramp_hits[0].rect.height)
                pos_height = max(pos_height, 0)



                target_y = hit.rect.y + hit.rect.height - pos_height

                if self.s.rect.bottom > target_y:
                    self.s.rect.bottom = target_y
                    self.s.pos.y = self.s.rect.bottom

        ring_hits = pygame.sprite.spritecollide(self.s, self.rings, False)
        
        
        
        if ring_hits:
            self.ring_count += 1
            print(self.ring_count)
            ring_hits[0].kill()

        pricks = pygame.sprite.spritecollide(self.s, self.spikes, False)

        if pricks:
            for prick in pricks:
                if self.s.vel.y > 0 and self.s.rect.bottom > prick.rect.top:
                    if self.ring_count > 0:
                        self.ring_count = self.ring_count / 2
                        r = Ring(self, self.s.pos.x - 180, self.s.rect.centery)
                        self.rings.add(r)
                        self.sprites.add(r)
                        self.window.blit(r.image, (self.s.pos.x - 180, self.s.rect.centery))
                    else:
                        pass
                    self.s.rect.bottom = prick.rect.top
                    self.s.pos.y = self.s.rect.bottom
                    self.s.pos.x = (prick.rect.left - 50)
                    self.s.vel.y = 0
                    self.s.vel.x = 0
                    self.ring_count = 0
                if self.s.vel.x > 0 and self.s.rect.right > prick.rect.left:
                    self.s.rect.right = (prick.rect.left - 50)
                    self.s.pos.x = self.s.rect.right
                    self.s.vel.x = 0
                    self.s.vel.y = 0
                if self.s.vel.x < 0 and self.s.rect.left < prick.rect.right:
                    self.s.rect.left = (prick.rect.right + 50)
                    self.s.pos.x = self.s.rect.left
                    self.s.vel.x = 0
                    self.s.vel.y = 0

        self.camera.update(self.s)

        # TODO: create an exploding list that generates rings (done)

        clashes = pygame.sprite.spritecollide(self.s, self.enemies, False)

        if clashes:
            for clash in clashes:
                if self.s.vel.y > 0 and abs(clash.rect.top - self.s.rect.bottom) < 5:
                    self.s.vel.y = 0
                    clash.vel = 0
                    self.s.rect.bottom = clash.rect.top
                    self.s.pos.y = self.s.rect.bottom
                    clash.kill()

                if abs(self.s.rect.left - clash.rect.right) < 10:
                    if self.ring_count > 0:
                        self.ring_count = self.ring_count / 2
                        r = Ring(self.s.pos.x + 80, self.s.rect.centery)
                        self.rings.add(r)
                        self.sprites.add(r)
                        self.window.blit(r.image, (self.s.pos.x + 80, self.s.rect.centery))
                    else:
                        pass
                    self.s.rect.left = (clash.rect.right + 50)
                    self.s.pos.x = self.s.rect.left
                    clash.vel = (clash.vel * -1)
                    self.ring_count = 0 
                    # TODO: study collisions with moving objects
                    print(self.ring_count)
                
                if abs(self.s.rect.right - clash.rect.left) < 10:
                    if self.ring_count > 0:
                        self.ring_count = self.ring_count / 2
                        r = Ring(self.s.pos.x - 80, self.s.rect.centery)
                        self.rings.add(r)
                        self.sprites.add(r)
                        self.window.blit(r.image, (self.s.pos.x - 80, self.s.rect.centery))
                    else:
                        pass
                    
                    self.s.rect.right = (clash.rect.left - 50)
                    self.s.pos.x = self.s.rect.right
                    clash.vel = (clash.vel * -1)
                    self.ring_count = 0 
                    # TODO: study collisions with moving objects

        RING_TOTAL = self.ring_count       


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                 
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP:
            #         self.index = (self.index + 1) % len(self.trainer)

            # if event.type == pygame.KEYUP: 
            #     if event.key == pygame.K_SPACE:
            #         self.s.limit_jump()

    def game_over():
        pass

    def start():
        pass




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




# with open(path.join(maps_dir, 'plats.txt'), 'r') as f:
#     data = f.readlines()

#     for line in data:
#         p = Platform(int(data[0]), int(data[0]), SMALL)
#         plats.add(p)
#         platforms.append(p)
    

# ramp = Ramp(940, HEIGHT - 50, 160, 160)
# ramp2 = Ramp(2500, HEIGHT - 50, 300, 300)
# ramps = pygame.sprite.Group()
# ramps.add(ramp)
# ramps.add(ramp2)


# loops
# loop = Loop(2000, HEIGHT - 50)
# loops = pygame.sprite.Group()
# loops.add(loop)  


# rings
# ring = Ring(100, HEIGHT - 120)
# ring_x_offset = 50
# ring_y = HEIGHT - 120

# ring_x_distance = 500



# for i in range(150):
#     ring_x_offset += 50
#     print(ring_x_offset)
#     ring = Ring(ring_x_offset, ring_y)
#     rings.add(ring)
#     if ring_x_offset > 150:
#         ring = Ring(ring_x_distance, ring_y)
#         rings.add(ring)

# TODO: figure out a way to blit the camera (done)


g = Game()

while g.running:
    g.new_game()

pygame.quit()