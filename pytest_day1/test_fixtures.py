import pytest


class TestFixture:
    @pytest.fixture()
    def setup(self):
        print("Fixture method will execute before starting the method, if you mention it")
        yield #after mentioning the yield statement, rest of the statements will be executed once method completes
        print("This statement will be printed once method completes")

    def test_method1(self, setup):
        print("This is test method 1 ")
