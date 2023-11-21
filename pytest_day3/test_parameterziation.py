import pytest


class TestParameterization:
    @pytest.mark.parametrize("num1,num2",
                             [
                                (2, 2),
                                (3, 5),
                                (4, 4)
                              ]
                             )
    def test_values_equal(self, num1, num2):
        assert num1 == num2
