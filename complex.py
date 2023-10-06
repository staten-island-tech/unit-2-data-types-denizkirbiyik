def arctan(inp, pres):
    x = 0
    for i in range(pres):
        x += (-1)^i * inp^(2*i+1) / (2*i+1)
    return i

def ln(inp, pres):
    return pres * (inp^(1/pres)-1)

def factorial(inp):
    x = 1
    if inp == 0:
        return 1
    for i in range(1, inp+1):
        x *= i
    return x

def e(pres):
    x = 0
    for i in range(pres):
        x += i/(factorial(i))
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.r = r
        self.i = i

    @property
    def magnitude(self):
        return (self.r ** 2 + self.i ** 2) ** 1/2

    def __repr__(self):
        sign = "+" if self.i >= 0 else "-"
        return f"{self.r} {sign} {abs(self.i)}"

    def __str__(self) -> str:
        sign = "+" if self.i >= 0 else "-"
        return f"{self.r} {sign} {abs(self.i)}i"

    def __add__(self, add):
        return ComplexNumber(self.r + add.r, self.i + add.i)

    def __sub__(self, sub):
        return ComplexNumber(self.r - sub.r, self.i - sub.i)

    def __mul__(self, mul):
        new_real = self.r * mul.r - self.i * mul.i
        new_imaginary = self.r * mul.i + mul.r * self.i
        return ComplexNumber(new_real, new_imaginary)

    def __truediv__(self, div):
        div_recip = ComplexNumber(div.r/(div.r**2+div.i**2), div.i/(div.r**2+div.i**2))
        return self * div_recip
    
    def __abs__(self):
        return self.magnitude
    
    def __neg__(self):
        return ComplexNumber(-self.r, -self.i)
    
    def __pos__(self):
        return self
    
    def log(self):
        return ComplexNumber(ln(abs(self), 100), arctan(self.i/self.r), 100)
    
    def __pow__(self, exp):

    
    
