import sys
from typing import Dict, Any

import pygame
import math

# Добавляем второй шарик. И пишем соударение шаров.
# Соударение шаров рассчитывается так: нужно разложить движение по двум осям:
# одна - это нормаль контакта, т.к. перпендикуляр к поверхности в точке контакта
# (в нашем случае, это будет прямая, проходящая через центры шаров), вторая ось - перпендикуляр к первой.
# Так вот, при упругом соударении, движение по первой оси изменится также, как если это былобы лобовое соударение шаров,
# а по второй - не изменится.

class Matrix:
    def __init__(self, a1, a2, a3, a4):
        self.A = [a1, a2, a3, a4]

    def return_determinant(self):
        return self.A[0]*self.A[3] + self.A[1]*self.A[2]

    def minor(self):
        self.A[0], self.A[3] = self.A[3], self.A[0]
        self.A[1], self.A[2] = self.A[2], self.A[1]

    def adjunct(self):
        self.A[1] *= -1
        self.A[2] *= -1

    def transpone(self):
        self.A[1], self.A[2] = self.A[2], self.A[1]

    def inverse(self):
        d = self.return_determinant()
        self.minor()
        self.adjunct()
        self.transpone()
        if d != 0:
            for i in self.A:
                i /= d


class Vector:
    """
    Simple 2D Vector. Yes, I know it can be easily made into multiple-vector by using tuples,
    but for this lab I only need simple 2D vector
    I keep it as simple and obvious as possible to better understand what I’m doing
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dot_product(self, other):
        """
        returns scalar (inner, dot) product (int or float)
        :param other: Vector
        :return: int or float
        >>> a = Vector(2, 2)
        >>> b = Vector(2, 3)
        >>> c = a * b
        >>> print(c)
        10
        """
        result = (self.x * self.y) + (other.x * other.y)
        return result

    def scalar_vector_mult(self, other):
        """
        returns scalar-vector product as new Vector
        :param other: int or float
        :return: Vector
        >>> a = Vector(1, 2)
        >>> b = 10
        >>> c = a * b
        >>> print(c.x, c.y)
        10 20
        """
        result = Vector()
        result.x = self.x * other
        result.y = self.y * other
        return result

    def length(self):
        """
        returns length of vector
        :return: float
        >>> a = Vector(5, 12)
        >>> a.length()
        13.0
        """
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        """
        :return: float
        >>> a = Vector(5, 12)
        >>> a.normalize()
        (0.38461538461538464, 0.9230769230769231)
        """
        norm_x = self.x / self.length()
        norm_y = self.y / self.length()
        return norm_x, norm_y


    def __add__(self, other):
        """
        Returns the vector addition of self and other
        :type other: Vector
        >>> a = Vector(1, 2)
        >>> b = Vector(1, 3)
        >>> c = a + b
        >>> print(c.x, c.y)
        2 5
        """
        result = Vector()
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result

    def __sub__(self, other):
        """
        Returns the vector subtraction of self and other
        :type other: Vector
        >>> a = Vector(1, 2)
        >>> b = Vector(1, 3)
        >>> c = a - b
        >>> print(c.x, c.y)
        0 -1
        """
        result = Vector()
        result.x = self.x - other.x
        result.y = self.y - other.y
        return result

    def __mul__(self, other):
        """
        if multiplied by number, returns scalar-vector product (vector)
        if multiplied by other vector, returns scalar product (int or float)
        """
        if type(other) == type(self):
            return self.dot_product(other)
        if type(other) == type(1) or type(other) == type(1.0):
            return self.scalar_vector_mult(other)

class Ball:
    def __init__(self, x, y, radius, balls_list=[]):
        """
        :type x: int
        :type y: int
        :type radius: int
        """
        self.position = Vector(x, y)
        self.velocity = Vector()
        self.radius = radius
        self.balls = balls_list

    def _update_friction(self, friction):
        """
        :param friction: float
        >>> a = Ball(30, 30, 10)
        >>> a.velocity = Vector(30, 30)
        >>> a._update_friction(0.3)
        >>> print(a.velocity.x, a.velocity.y)
        9.0 9.0
        """
        self.velocity *= friction

    def _change_coord(self, dt):
        """
        update position according to velocity and FPS (clock tick / 1000)
        :param dt: float
        >>> dt = 50 / 1000.0
        >>> a = Ball(10, 10, 5)
        >>> a.velocity = Vector(100, 100)
        >>> a._change_coord(dt)
        >>> print(a.position.x, a.position.y)
        15.0 15.0
        """
        self.position += self.velocity * dt

    def _bounce_walls(self, width, height):
        if self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= -1
        if self.position.x < 0 + self.radius:
            self.position.x = 0 + self.radius
            self.velocity.x *= -1
        if self.position.y > height - self.radius:
            self.position.y = height - self.radius
            self.velocity.y *= -1
        if self.position.y < 0 + self.radius:
            self.position.y = 0 + self.radius
            self.velocity.y *= -1

    def _bounce_others(self):
        for ball in self.balls:
            if ball != self:
                path = self.position - ball.position
                distance = path.length() - (self.radius + ball.radius)
                if distance <= 0:
                    # Создаём новый базис и раскладываем его по осям координат:
                    collapse_direction = Vector(*path.normalize())
                    cross_direction = Vector(collapse_direction.y, - collapse_direction.x)
                    # collapse_direction и cross_direction — ортонормированные векторы
                    # раскладываем velocity по новому базису
                    # находим матрицу перехода между базисами
                    A = Matrix(collapse_direction.x, collapse_direction.y, cross_direction.x, cross_direction.y)
                    if A.return_determinant() != 0 and A.return_determinant() != 0.0:
                        A.inverse()
                        # находим вектор движения в новом базисе
                        newbasis_velocity = Vector()
                        newbasis_velocity.x = (A.A[0] * self.velocity.x) + (A.A[2] * self.velocity.y)
                        newbasis_velocity.y = (A.A[1] * self.velocity.x) + (A.A[3] * self.velocity.y)
                        collapse_direction.x, collapse_direction.y = -collapse_direction.x, -collapse_direction.y # bounce
                        # собираем обратно
                        new_velocity = Vector()
                        new_velocity.x = (collapse_direction.x * newbasis_velocity.x) + (cross_direction.x * newbasis_velocity.y)
                        new_velocity.y = (collapse_direction.y * newbasis_velocity.x) + (cross_direction.y * newbasis_velocity.y)
                        self.velocity = new_velocity
                    else:
                        self.velocity.x *= -1
                        self.velocity.y *= -1


    def draw(self, screen):
        """
        Draws the ball in its position in color defined by speed
        """
        self.green = 255 if int(abs(self.velocity.x)) >= 255 else int(abs(self.velocity.x))
        self.blue = 255 if int(abs(self.velocity.y)) >= 255 else int(abs(self.velocity.y))
        pygame.draw.circle(screen, (150, self.green, self.blue), (int(self.position.x), int(self.position.y)), self.radius)

    def input(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.velocity.x -= 10
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.velocity.x += 10
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.velocity.y -= 10
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.velocity.y += 10


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    pygame.init()

    width = 500
    height = 500

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('YAHOOOO')
    clock = pygame.time.Clock()

    frict = 0.99
    balls = []

    balls.append(Ball(30, 30, 20, balls))
    balls.append(Ball(480, 480, 10, balls))

    while True:
        dt = clock.tick(50) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                balls.append(Ball(x, y, 15, balls))

        screen.fill((0, 0, 0))

        for ball in balls:
            ball.input()
        for ball in balls:
            ball._bounce_walls(width, height)
        for ball in balls:
            ball._bounce_others()
        for ball in balls:
            ball._change_coord(dt)
        for ball in balls:
            ball._update_friction(frict)
        for ball in balls:
            ball.draw(screen)

        pygame.display.flip()