import sys, pygame, math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        """
        >>> print(Vector(1, 2))
        (1, 2)
        """
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, other):
        """
        Returns the vector addition of self and other
        :type other: Vector
        >>> print(Vector(1, 2) + Vector(1, 3))
        (2, 5)
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Returns the vector subtraction of self and other
        :type other: Vector
        >>> print(Vector(1, 2) - Vector(1, 3))
        (0, -1)
        """
        return Vector(self.x - other.x, self.y - other.y)

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
        >>> print(Vector(5, 12).normalize())
        (0.38461538461538464, 0.9230769230769231)
        """
        return Vector(self.x / self.length(), self.y / self.length())

    def dot_product(self, other):
        """
        returns scalar (inner, dot) product (int or float)
        :param other: Vector
        :return: int or float
        >>> print(Vector(2, 2) * Vector(2, 3))
        10
        """
        return (self.x * other.x) + (self.y * other.y)

    def scalar_vector_mult(self, num):
        """
        returns scalar-vector product as new Vector
        :param num: int or float
        :return: Vector
        >>> print(Vector(1, 2) * 10)
        (10, 20)
        """
        return Vector(self.x * num, self.y * num)

    def __mul__(self, other):
        """
        if multiplied by number, returns scalar-vector product (vector)
        if multiplied by other vector, returns scalar product (int or float)
        """
        if type(other) == type(self):
            return self.dot_product(other)
        if type(other) == type(1) or type(other) == type(1.0):
            return self.scalar_vector_mult(other)

    def __rmul__(self, other):
        """ Called if 4*self for instance """
        return self.__mul__(other)

    def __neg__(self):
        """
        >>> print(-Vector(1, -2))
        (-1, 2)
        """
        return Vector(-self.x, -self.y)

    def intpair(self):
        return int(self.x), int(self.y)


def find_mass_center(*args):
    """
    >>> print(find_mass_center(Vector(1, 2), Vector(2, 1), Vector(2, 3), Vector(5, 6), Vector(8, 7), Vector(-2, -2), Vector(4, -1)))
    (2.857142857142857, 2.2857142857142856)
    """
    return Vector(sum([dot.x for dot in args]) / len(args), sum([dot.y for dot in args]) / len(args))


class Ball:
    def __init__(self, x, y, radius):
        """
        :type x: int
        :type y: int
        :type radius: int
        """
        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.radius = radius
        self.selected = False

    def input(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.velocity.x -= 10
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.velocity.x += 10
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.velocity.y -= 10
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.velocity.y += 10

    def update(self, dt, frict):
        """
        update position according to velocity and FPS (clock tick / 1000)
        :param dt: float
        :param frict: float
        """
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

        self.velocity *= frict
        self.position += self.velocity * dt

    def update_selection(self, old_selection):
        if isinstance(old_selection, Ball):
            old_selection.selected = False
        self.selected = True

    def check_collision(self, other):
        path = self.position - other.position
        distance = path.length() - (self.radius + other.radius)
        if distance <= 0:
            norm = path.normalize()
            self_p = self.velocity * self.radius
            other_p = other.velocity * other.radius
            self_dp = (((other.radius * -2) / (self.radius + other.radius) * self_p +
                       (self.radius * 2) / (self.radius + other.radius) * other_p) * norm) * norm
            other_dp = (((self.radius* 2) / (self.radius + other.radius) * other_p  +
                         (other.radius * -2) / (self.radius + other.radius) * self_p) * norm) *norm
            self.velocity += self_dp * (1 / (2 * self.radius))
            other.velocity += other_dp * (1 / (2 * other.radius))


    def render(self, canvas):
        # velocity = self.velocity.intpair()
        position = self.position.intpair()

        # red = 150
        # green = 255 if abs(velocity[0]) >= 255 else abs(velocity[0])
        # blue = 255 if abs(velocity[1]) >= 255 else abs(velocity[1])

        if self.selected:
            self.red, self.green, self.blue = 150, 50, 50
        else:
            self.red, self.green, self.blue = 150, 20, 20

        pygame.draw.circle(canvas, (self.red, self.green, self.blue), (position[0], position[1]), self.radius)


def mouse_click_action(balls_list, current_selection, cursor_position):
    """
    select ball and unselect previously selected
    if non selected create new
    return selected ball
    :param current_selection: Ball
    :return Ball
    """
    for ball in balls_list:
        distance = cursor_position - ball.position
        if distance.length() <= ball.radius:
            ball.update_selection(current_selection)
            return ball
    new_ball = Ball(*cursor_position.intpair(), 15)
    balls_list.append(new_ball)
    new_ball.update_selection(current_selection)
    return new_ball


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    pygame.init()

    width = 500
    height = 500

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('YAHOOOO')
    clock = pygame.time.Clock()

    friction = 0.99
    balls = list()
    balls.append(Ball(30, 30, 20))
    balls.append(Ball(480, 480, 10))

    selection = None

    while True:
        dt = clock.tick(50) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                click = Vector(*pygame.mouse.get_pos())
                selection = mouse_click_action(balls, selection, click)



        screen.fill((0, 0, 0))

        for ball in balls:
            if ball.selected:
                ball.input()
        other_balls = [x for x in balls]
        for ball in balls:
            other_balls.remove(ball)
            for other_ball in other_balls:
                ball.check_collision(other_ball)
        for ball in balls:
            ball.update(dt, friction)
        for ball in balls:
            ball.render(screen)

        pygame.display.flip()
