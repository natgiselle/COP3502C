from base_classes import *

class SecureAccount(Account):
    def __init__(self, password):
        super().__init__()
        self._password = password

    def get_balance(self, password):
        if password != self._password:
            print("Incorrect password")
            return
        return super().get_balance()

    def deposit(self, amount, password):
        if password != self._password:
            print("Incorrect password")
            return
        super().deposit(amount)

    def withdraw(self, amount, password):
        if password != self._password:
            print("Incorrect password")
            return
        super().withdraw(amount)


class MemoryCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self._result = 0

    def add(self, x, y):
        if x == "RESULT":
            x = self._result
        if y == "RESULT":
            y = self._result
        self._result = super().add(x, y)
        return self._result

    def sub(self, x, y):
        if x == "RESULT":
            x = self._result
        if y == "RESULT":
            y = self._result
        self._result = super().sub(x, y)
        return self._result


class ImprovedFraction(Fraction):
    def __init__(self, numerator, denominator):
        super().__init__(numerator, denominator)

    def add(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        result = super().add(other)
        result.__class__ = ImprovedFraction
        return result

    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        result = super().multiply(other)
        result.__class__ = ImprovedFraction
        return result

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __str__(self):
        return f"{self.get_numerator()}/{self.get_denominator()}"
    