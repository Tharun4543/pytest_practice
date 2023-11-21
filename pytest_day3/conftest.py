import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    print("Launching browser")
    return "chrome hasbeen lauched"


@pytest.fixture()
def browser_setup():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture()
def browser_setup_cli(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Firefox()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config.project_name = "Pytest_Practice"
    config.module_name = "pytest_day3"
    config.tester = "Tharun Nagiri"


def pytest_metadata(config):
    if 'JAVA-HOME' in config.option.metadata:
        del config.option.metadata['JAVA-HOME']

    if 'plugins' in config.option.metadata:
        del config.option.metadata['plugins']
