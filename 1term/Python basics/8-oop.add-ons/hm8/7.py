class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real, self.imaginary * other.imaginary)

    def __str__(self):
        return f'({self.real}+j{self.imaginary})'


num1 = Complex(1, 2)
num2 = Complex(3, 4)
print(num1 + num2)
print(num1 * num2)
