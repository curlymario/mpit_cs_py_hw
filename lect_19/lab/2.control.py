import sys
import pygame

# Добавим управление: пусть при нажатой клавише-стрелке, у шарика появляется ускорение в соответствующую сторону.
# Испульзуйте список pygame.key.get_pressed().

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()

x = 30
y = 30
vx = 0
vy = 0
radius = 20
frict = 0.1

while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()

# Управление
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        vx -= 10
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        vx += 10
    if pygame.key.get_pressed()[pygame.K_UP]:
        vy -= 10
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        vy += 10

    x += vx * dt
    y += vy * dt

# Проверка на выход за край
    if x >= width - radius or x <= 0 + radius:
        vx *= -1
    if y >= height - radius or y <= 0 + radius:
        vy *= -1

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (150, 10, 50), (int(x), int(y)), radius)

    pygame.display.flip()