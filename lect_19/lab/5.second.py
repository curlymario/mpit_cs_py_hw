import sys
import pygame

# Добавляем второй шарик. И пишем соударение шаров.
# Соударение шаров рассчитывается так: нужно разложить движение по двум осям:
# одна - это нормаль контакта, т.к. перпендикуляр к поверхности в точке контакта
# (в нашем случае, это будет прямая, проходящая через центры шаров), вторая ось - перпендикуляр к первой.
# Так вот, при упругом соударении, движение по первой оси изменится также, как если это былобы лобовое соударение шаров,
# а по второй - не изменится.

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()

frict = 0.01
balls = []

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.velocity = Vector(0, 0)
        self.radius = radius
        balls.append(self)

    def _update_friction(self, frict):
        if self.velocity.x != 0:
            self.velocity.x -= frict * self.velocity.x
        if self.velocity.y != 0:
            self.velocity.y -= frict * self.velocity.y

    def _change_coord(self, dt):
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt

    def _bounce_walls(self, width, height):
        if self.x > width - self.radius:
            self.x = width - self.radius
            self.velocity.x *= -1
        if self.x < 0 + self.radius:
            self.x = 0 + self.radius
            self.velocity.x *= -1
        if self.y > height - self.radius:
            self.y = height - self.radius
            self.velocity.y *= -1
        if self.y < 0 + self.radius:
            self.y = 0 + self.radius
            self.velocity.y *= -1

    def draw(self, screen):
        self.green = 255 if int(abs(self.velocity.x)) >= 255 else int(abs(self.velocity.x))
        self.blue = 255 if int(abs(self.velocity.y)) >= 255 else int(abs(self.velocity.y))
        pygame.draw.circle(screen, (150, self.green, self.blue), (int(self.x), int(self.y)), self.radius)


    def input(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.velocity.x -= 10
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.velocity.x += 10
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.velocity.y -= 10
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.velocity.y += 10

    def move(self, dt, frict, width, height):
        self._change_coord(dt)
        self._update_friction(frict)
        self._bounce_walls(width, height)


b1 = Ball(30, 30, 20)
b2 = Ball(480, 480, 10)

while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()

    screen.fill((0, 0, 0))

    for ball in balls:
        ball.input()
        ball.move(dt, frict, width, height)
        ball.draw(screen)

    pygame.display.flip()