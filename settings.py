import pygame

# game properties
WIDTH = 800
HEIGHT = 600
FPS = 60



# colors
BLACK = (0, 0, 0)
YELLOW = (239, 245, 66)
BLUE = (0, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
CYAN = (116, 205, 174)

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
    (2650, HEIGHT - 250, SMALL),
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
    (11900, HEIGHT - 50, 254, 254, 1)  
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
    (9020, HEIGHT - 320), 
    (9050, HEIGHT - 320), 
    (9080, HEIGHT - 320), 
    (12020, HEIGHT - 320), 
    (12100, HEIGHT - 320), 
    (12180, HEIGHT - 320), 
    (12520, HEIGHT - 320), 
    (12550, HEIGHT - 320), 
    (12580, HEIGHT - 320), 
    (13180, HEIGHT - 70), 
    (13220, HEIGHT - 70), 
    (13260, HEIGHT - 70), 



    ]


ring_offset = 50

for i in range(2):
    RING_LIST.append((RING_X + ring_offset, HEIGHT - 150))
    ring_offset += 50
   

# Spike properties
SPIKE_LIST = [
    (550, HEIGHT - 50),
    (1650, HEIGHT - 200),
    (2600, HEIGHT - 50),
    (3200, HEIGHT - 50),
    (3700, HEIGHT - 50),
    (5170, HEIGHT - 200),

]

# enemy properties
ENEMY_LIST = [
    (375, HEIGHT - 50),
    (1400, HEIGHT - 200),
    (2300, HEIGHT - 50),
    (4090, HEIGHT - 300),
    (5500, HEIGHT - 200),
    (7863, HEIGHT - 200),
]

# Player properties
HALF_P_WIDTH = 25
PREVIOUS_POS = [0, 0]
RING_COUNT = 0
PLAYER_JUMP = 11