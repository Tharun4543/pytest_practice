import pytest


class TestSample:
    @pytest.mark.run(order=3)
    def test_multiply(self):
        print(10 * 2)

    @pytest.mark.run(order=4)
    def test_division(self):
        print(10 // 2)

    @pytest.mark.run(order=1)
    def test_addition(self):
        print(10 + 20)

    @pytest.mark.run(order=2)
    def test_subtract(self):
        print(10 - 2)
