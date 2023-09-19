import pytest
from selenium import webdriver
from pytest_bdd import given, then, parsers
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--env_name", action='store', default="staging")
    parser.addoption("--product_name", action='store', default="quartz")


@pytest.fixture(scope='class')
def setup_one(request):
    browser = request.config.getoption("browser_name")
    env = request.config.getoption("env_name")
    product = request.config.getoption("product_name")


    if browser == "chrome" and env == "staging":
        service = Service(executable_path=r"C:\Users\harshalashok_warkar\study_codes\pytest_bdd_demo\drivers\chromedriver.exe")
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        driver.get("https://www.thetestingworld.com/testings/")
        driver.maximize_window()
        request.cls.driver = driver
        request.cls.env = env
        yield
        driver.close()






# @given("the initial value is 0", target_fixture="setupone")
# def given_initial_value_is_zero():
#     return {"value": 0}