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


    def test_division_calculate_correctly(self):
        assert  self.calc.division(self,4,2) == 2

    def test_division_failed(self):
        assert  self.calc.division(self,5,2) == 2

    def test_division_by_zero(self):
        assert  self.calc.division(self,4,0) == 0

    def test_substraction_calculate_correctly(self):
        assert self.calc.subtraction(self,4,2) == 2

    def test_substraction_failed(self):
        assert  self.calc.subtraction(self,5,5) == 2

    def test_adding_calculate_correctly(self):
        assert  self.calc.adding(self,2,2) == 4

    def test_adding_failed(self):
        assert self.calc.adding(self,2,2) == 5