# from unittest import TestCase
#
#
# class TestClass(TestCase):
#     def test1(self):
#         self.assertTrue(True)

def test1():
    assert True


def test2():
    assert (1, 2, 3) == (1, 2, 3)


def test3():
    assert (1, 2, 3) == (1, 2)


def test4():
    assert 25 == 25


def test5():
    assert 15 == 16


def test6():
    assert 1 in [1, 2, 3]
