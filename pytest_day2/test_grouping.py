import pytest


class TestGrouping:
    @pytest.mark.regression
    def test_regression(self):
        print("This is regression method")

    @pytest.mark.regression
    def test_regression_2(self):
        print("This is one more regression method")

    @pytest.mark.sanity
    def test_sanity(self):
        print("This is sanity method")

    @pytest.mark.regression
    def test_sanity_2(self):
        print("This is one more sanity method")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_sanity_reg(self):
        print("This is sanity and regression method")
