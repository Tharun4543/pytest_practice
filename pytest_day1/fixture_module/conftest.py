import pytest


@pytest.fixture()
def setup():
    print("This is confest fixture we can use for all classes under a same directory")
