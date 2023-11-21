import pytest


class TestSample:
    @pytest.mark.third
    def test_multiply(self):
        print(10 * 2)

    @pytest.mark.fourth
    def test_division(self):
        print(10 // 2)

    @pytest.mark.first
    def test_addition(self):
        print(10 + 20)

    @pytest.mark.second
    def test_subtract(self):
        print(10 - 2)
