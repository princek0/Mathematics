class Cnumber:

    def __init__(self, real=0, imaginary=0):  # Real and imaginary parts of the number.
        self.re = real
        self.im = imaginary

    def __str__(self):
        if self.re != 0:
            if self.im > 0:
                return "{} {} {}i".format(self.re, "+", self.im)
            elif self.im == 0:
                return "{}".format(self.re)
            else:
                return "{} {} {}i".format(self.re, "-", abs(self.im))
        else:
            return "{}i".format(self.im)

    def __add__(self, other):  # Complex addition.
        return Cnumber(self.re + other.re, self.im + other.im)

    def __sub__(self, other):  # Complex subtraction.
        return Cnumber(self.re - other.re, self.im - other.im)

    def __neg__(self):  # Negation.
        return Cnumber(-self.re, -self.im)

    def __mul__(self, other):  # Complex multiplication.
        real = self.re * other.re - self.im * other.im
        imaginary = self.im * other.re + self.re * other.im
        return Cnumber(real, imaginary)

    def conjugate(self):  # Returns the complex conjugate of the number.
        return Cnumber(self.re, -self.im)

    def __truediv__(self, other):  # Complex division.
        conjugate = other.conjugate()
        denominator = (other * conjugate).re
        numerator = self * conjugate

        return Cnumber(numerator.re / denominator, numerator.im / denominator)

    def real(self):  # Returns real part of the number.
        return self.re

    def imaginary(self):  # Returns imaginary part of the number.
        return "{}i".format(self.im)

    def modulus(self):  # Returns complex modulus of the number.
        math = __import__('math')
        return round(math.sqrt(self.re ** 2 + self.im ** 2), 5)

    def arg(self):  # Returns the angle the number makes with the real axis.
        math = __import__('math')
        angle = round(math.atan(self.im / self.re), 5)
        return angle

    def polar(self):  # Returns the polar form of the number.
        return "{}(cos({})+isin({}))".format(self.modulus(), self.arg(), self.arg())

    def sqrt(self):  # Returns the square root of the number in polar form.
        math = __import__('math')
        return "{}(cos({})+isin({}))".format(math.sqrt(self.modulus()), self.arg() / 2, self.arg() / 2)

    def exp(self, n):  # Returns the number to some exponent (n) in polar form.
        return "{}(cos({})+isin({}))".format(self.modulus() ** n, self.arg() * n, self.arg() * n)

    def __eq__(self, other):  # Compares whether both real and imaginary parts are equivalent.
        if self.re == other.re and self.im == other.im:
            return True
        else:
            return False

    def modeq(self, other):  # Compares whether moduli of numbers are equivalent.
        if self.modulus() == other.modulus():
            return True
        else:
            return False

    def __gt__(self, other):  # Compares moduli of numbers.
        if self.modulus() > other.modulus():
            return True
        else:
            return False

    def __lt__(self, other): # Compares moduli of numbers.
        if self.modulus() < other.modulus():
            return True
        else:
            return False

    def __ge__(self, other):  # Compares moduli of numbers.
        if self.modulus() >= other.modulus():
            return True
        else:
            return False

    def __le__(self, other):  # Compares moduli of numbers.
        if self.modulus() <= other.modulus():
            return True
        else:
            return False

    def matrix(self):  # Returns the matrix form of the number.
        M = [[self.re, -1 * self.im],
             [self.im, -1 * self.re]]

        return M

    @staticmethod
    def argand(*argv):  # Displays an argand diagram with the points plotted.
        import matplotlib.pyplot as plt
        import numpy as np

        # Points
        real = []  # X values.
        imaginary = []  # Y values.

        for arg in argv:
            real.append(arg.re)
            imaginary.append(arg.im)

        # Axis
        plt.axhline(y=0, color='black')
        plt.axvline(x=0, color='black')

        # Unit Circle
        r = 1
        n = 1000
        t = np.linspace(0, 2 * np.pi, n + 1)
        x = r * np.cos(t)
        y = r * np.sin(t)

        # Graph
        for arg in argv:  # Connects origin to points.
            plt.arrow(0, 0, arg.re, arg.im)

        for arg in argv:  # Annotates points.
            plt.annotate("({},{})".format(arg.re, arg.im), (arg.re, arg.im))

        plt.ylabel('Imaginary')
        plt.xlabel('Real')
        plt.axis("equal")
        plt.grid()
        plt.plot(x, y)
        plt.plot(real, imaginary, 'bo')
        plt.show()

    def rotate(self, angle):  # Returns the value of the number rotated about the origin.
        import math
        real = round(self.re * math.cos(angle) - self.im * math.sin(angle), 5)
        imaginary = round(self.re * math.sin(angle) + self.im * math.cos(angle), 5)

        return Cnumber(real, imaginary)

    def dilate(self, scale):  # Returns the value of the number dilated about the origin for some scale value.
        k = Cnumber(scale, 0)
        return k * self

    @staticmethod
    def area(polygon):  # Returns the area of the shape enclosed by the points; Points must be listed anticlockwise.
        n = len(polygon)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += polygon[i].re * polygon[j].im
            area -= polygon[j].re * polygon[i].im
        area = abs(area) / 2.0
        return area
