import  pytest
from app.calculator import Calculator

def multiply(x,y):
    return x*y


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self,2, 2) == 4

    def test_multiply_failed(self):
        assert  self.calc.multiply(self,2,2) == 5


    