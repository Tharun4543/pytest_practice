import pytest


class TestSample:
    def test_addition(self):
        print(10 + 20)

    @pytest.mark.skip
    def test_subtract(self):
        print(10 - 2)
