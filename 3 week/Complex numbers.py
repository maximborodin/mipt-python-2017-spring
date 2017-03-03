import sys


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __mul__(self, other):
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real
        )

    def __sub__(self, other):
        return ComplexNumber(
            self.real - other.real,
            self.imaginary - other.imaginary
        )

    def __truediv__(self, other):
        if other.imaginary == 0.0:
            return ComplexNumber(
                self.real / other.real,
                self.imaginary / other.real
            )
        else:
            return self * ComplexNumber(other.real, -other.imaginary) / \
                   ComplexNumber(other.real ** 2 + other.imaginary ** 2, 0.0)

    def __str__(self):
        if self.real == 0.0 and self.imaginary == 0.0:
            return '0.00'
        elif self.real == 0.0:
            return "%.2f" % self.imaginary + 'i'
        elif self.imaginary == 0.0:
            return "%.2f" % self.real
        else:
            if self.imaginary > 0.0:
                return "%.2f" % self.real + ' + ' \
                       + "%.2f" % self.imaginary + 'i'
            else:
                return "%.2f" % self.real + ' - ' \
                       + "%.2f" % -self.imaginary + 'i'

# print(ComplexNumber(real=1.0, imaginary=0.0))
# print(ComplexNumber(real=0.0, imaginary=1.0))
# print(ComplexNumber(real=1.0, imaginary=1.0))
# print(ComplexNumber(real=2.0, imaginary=-2.0))
# print(ComplexNumber(real=1.0, imaginary=1.0)
# + ComplexNumber(real=2.0, imaginary=2.0))
# print(ComplexNumber(real=1.0, imaginary=1.0)
# + ComplexNumber(real=-1.0, imaginary=-1.0))
# print(ComplexNumber(real=1.0, imaginary=1.0)
# - ComplexNumber(real=1.0, imaginary=2.0))
# print(ComplexNumber(real=1.0, imaginary=0.0)
# * ComplexNumber(real=0.0, imaginary=1.0))
# print(ComplexNumber(real=10.0, imaginary=0.0)
# / ComplexNumber(real=-5.0, imaginary=0.0))

if __name__ == "__main__":
    for line in sys.stdin.readlines():
        print(eval(line.strip()))
