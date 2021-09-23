
class Calculator(object):
    num1 = int
    num2 = int

    @property
    def num1(self) -> int: return self.num1

    @property
    def num2(self) -> int: return self.num2

    @num1.setter
    def num1(self, num1): self.num1 = num1

    @num2.setter
    def num2(self, num2): self.num2 = num2