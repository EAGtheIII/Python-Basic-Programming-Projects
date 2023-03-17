Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)

    def __mul__(self, no):
        real = self.real * no.real
        imaginary = self.imaginary * no.imaginary
        return Complex(real, imaginary)

    def __truediv__(self, no):
        real = self.real / no.real
        imaginary = self.imaginary / no.imaginary
        return Complex(real, imaginary)

    def mod(self):
        real = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(real, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = '%.2f + 0.00i' % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = '0.00 + %.2fi' % (self.imaginary)
            else:
                result = '0.00 - %.2fi' % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = '%.2f + %.2fi' % (self.real, self.imaginary)
        else:
            result = '%.2f - %.2fi % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    C = map(float, input().split())
    D = map(float, input().split())
    x = Complex(*C)
    y = Complex(*D)
    print ('\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))) 