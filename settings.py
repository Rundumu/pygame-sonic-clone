import pygame

# game properties
WIDTH = 800
HEIGHT = 600
FPS = 60
window = pygame.display.set_mode((WIDTH, HEIGHT))


# colors
BLACK = (0, 0, 0)
YELLOW = (239, 245, 66)
BLUE = (0, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# physics
GRAVITY = 0.3
ACCEL = 1
FRICTION = -0.12
FASTER_TIME = 2000

# Platform properties
SMALL = (100, 50)
MEDIUM = (200, 100)
LARGE = (1000, 150)
GROUND = (100000, 100)

PLATFORM_LIST = [
    (1000, HEIGHT - 200, LARGE),
    (2900, HEIGHT - 300, SMALL),
    (3200, HEIGHT - 400, SMALL),
    (3500, HEIGHT - 400, SMALL),
    (4000, HEIGHT - 300, MEDIUM),
    (5000, HEIGHT - 200, LARGE),
    (5500, HEIGHT - 400, SMALL),
    (6700, HEIGHT - 450, SMALL),
    (6750, HEIGHT - 250, MEDIUM),
    (7500, HEIGHT - 200, LARGE),
    (8000, HEIGHT - 400, SMALL),
    (9000, HEIGHT - 300, SMALL),
    (12000, HEIGHT - 300, MEDIUM),
    (12500, HEIGHT - 300, SMALL),
    (15000, HEIGHT - 300, SMALL),
    ]

# Ramp properties

RAMP_LIST = [
    (950, HEIGHT - 50, 160, 160, 1),
    (2050, HEIGHT - 50, 160, 160, 2),
    (4950, HEIGHT - 50, 160, 160, 1),
    (6050, HEIGHT - 50, 160, 160, 2),
    (6850, HEIGHT - 250, 200, 200, 2),
    (7450, HEIGHT - 50, 160, 160, 1),
    (8500, HEIGHT - 50, 160, 160, 2),  
]


# Ring properties
RING_X = 500

RING_LIST = [
    (RING_X, HEIGHT - 150),
    (1500, HEIGHT - 320),
    (1550, HEIGHT - 320),
    (1600, HEIGHT - 320),        
    (2920, HEIGHT - 320), 
    (2940, HEIGHT - 320),        
    (2960, HEIGHT - 320), 
    (3230, HEIGHT - 420),        
    (3255, HEIGHT - 420),        
    (3280, HEIGHT - 420), 
    (3520, HEIGHT - 420),        
    (3550, HEIGHT - 420),        
    (3580, HEIGHT - 420),        
    (4020, HEIGHT - 320),        
    (4100, HEIGHT - 320),        
    (4180, HEIGHT - 320),        
    (5520, HEIGHT - 420),        
    (5550, HEIGHT - 420),        
    (5580, HEIGHT - 420), 
    (6720, HEIGHT - 470),        
    (6750, HEIGHT - 470),        
    (6780, HEIGHT - 470),
    (8020, HEIGHT - 420),        
    (8050, HEIGHT - 420),        
    (8080, HEIGHT - 420),        
    ]

ring_offset = 50

for i in range(2):
    RING_LIST.append((RING_X + ring_offset, HEIGHT - 150))
    ring_offset += 50
   

# Spike properties
SPIKE_LIST = []

# Player properties
HALF_P_WIDTH = 25
PREVIOUS_POS = [0, 0]
RING_COUNT = 0