import sys
import pygame

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()

x = 30
y = 30
vx = 50
vy = 50

while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            sys.exit()

    x += vx * dt
    y += vy * dt

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (150, 10, 50), (int(x), int(y)), 20)

    pygame.display.flip()