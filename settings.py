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
    (3000, HEIGHT - 300, SMALL),
    (3500, HEIGHT - 200, SMALL),
    (4000, HEIGHT - 300, MEDIUM),
    (5000, HEIGHT - 300, LARGE),
    (500, HEIGHT - 300, SMALL),
    (500, HEIGHT - 300, SMALL),
    (500, HEIGHT - 300, SMALL),
    (500, HEIGHT - 300, SMALL),
    (500, HEIGHT - 300, SMALL),
    (500, HEIGHT - 300, SMALL),
    (500, HEIGHT - 300, SMALL),
    (500, HEIGHT - 300, SMALL),
    (500, HEIGHT - 300, SMALL),
    (500, HEIGHT - 300, SMALL),
    (500, HEIGHT - 300, SMALL),
    (500, HEIGHT - 300, SMALL),
    (500, HEIGHT - 300, SMALL),
    (500, HEIGHT - 300, SMALL),
    (500, HEIGHT - 300, SMALL),
]
# Ring properties
RING_X = 50

RING_LIST = [(RING_X, HEIGHT - 150), 
            ]

ring_offset = 50

iter_count = 0

for i in range(3):
    RING_LIST.append((RING_X + ring_offset, HEIGHT - 150))
    ring_offset += 50
   

# Player properties
HALF_P_WIDTH = 25
PREVIOUS_POS = [0, 0]
RING_COUNT = 0