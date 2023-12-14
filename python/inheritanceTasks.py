class Fraction:
    def __init__(self, numerator, denominator):
        self.a = numerator
        self.b = denominator

    def numerator(self, number=None):
        if number:
            self.a = number
        return self.a

    def denominator(self, number=None):
        if number:
            self.b = number
        return self.b

    def __str__(self):
        return f"{self.a}/{self.b}"

    def __repr__(self):
        return f"Fraction({self.a}, {self.b})"


fraction = Fraction(3, 9)
print(fraction, repr(fraction))
print(fraction.denominator())
print(fraction.numerator())
print(fraction.numerator('20'))
