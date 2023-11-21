import pytest


class TestFixturePractice1:
    def test_method1(self, setup):
        print("This is test fixture practice 1 method 1 ")

    def test_method2(self, setup):
        print("This is test fixture practice 1 method 2 ")

    def test_method3(self, setup):
        print("This is test fixture practice 1 method 3 ")
