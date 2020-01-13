
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

    def dot_product(self, other):
        """
        returns scalar (inner, dot) product (int or float)
        :param other: Vector
        :return: int or float
        >>> print(Vector(2, 2) * Vector(2, 3))
        10
        """
        return (self.x * self.y) + (other.x * other.y)

    def scalar_vector_mult(self, num):
        """
        returns scalar-vector product as new Vector
        :param other: int or float
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


def find_mass_center(*args):
    """
    >>> print(find_mass_center(Vector(1, 2), Vector(2, 1), Vector(2, 3), Vector(5, 6), Vector(8, 7), Vector(-2, -2), Vector(4, -1)))
    (2.857142857142857, 2.2857142857142856)
    """
    return Vector(sum([dot.x for dot in args]) / len(args), sum([dot.y for dot in args]) / len(args))

if __name__ == '__main__':
    import doctest

    doctest.testmod()

