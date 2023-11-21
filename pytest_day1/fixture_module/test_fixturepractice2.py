import pytest


class TestFixturePractice2:
    def test_method1(self, setup):
        print("This is test fixture practice 2 method 1 ")

    def test_method2(self, setup):
        print("This is test fixture practice 2 method 2 ")

    def test_method3(self, setup):
        print("This is test fixture practice 2 method 3 ")
