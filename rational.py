from math import gcd

class Rational:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ValueError("Cannot divide by zero.")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Rational(new_numerator, new_denominator)
        return NotImplemented

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Rational({self.numerator}, {self.denominator})"

# Example usage
if __name__ == "__main__":
    r1 = Rational(3, 4)
    r2 = Rational(5, 6)

    print(f"R1: {r1}")                # Output: R1: 3/4
    print(f"R2: {r2}")                # Output: R2: 5/6
    print(f"R1 + R2: {r1 + r2}")      # Output: R1 + R2: 19/24
    print(f"R1 - R2: {r1 - r2}")      # Output: R1 - R2: -1/24
    print(f"R1 * R2: {r1 * r2}")      # Output: R1 * R2: 15/24
    print(f"R1 / R2: {r1 / r2}")      # Output: R1 / R2: 18/20
