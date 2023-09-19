import pytest
from pytest_bdd import *
from selenium.webdriver.common.by import By

# from access import BaseOne

scenarios('../features')

# @scenario('../features/Registration.feature', 'Registration with valid data')
# def test_publish():
#     print("hello")


@pytest.mark.usefixtures("setup_one")
class TestWhatsAppWrongKycRiskProfileRetake():
    @given(u': User is on Registration page')
    def step_impl(self, setupone):
        self.driver.get("https://www.thetestingworld.com/testings/")


    @when(u': User entered username')
    def step_impl(self):
        self.driver.find_element(By.XPATH, "//input[@name='fld_username']").send_keys("Har")

    @when(u': User entered email id')
    def step_impl(self):
        self.driver.find_element(By.XPATH, "//input[@name='fld_email']").send_keys("Har@gmail.com")


    @when(u': User entered password')
    def step_impl(self):
        self.driver.find_element(By.XPATH, "//input[@name='fld_password']").send_keys("har@1234")


    @when(u': User click on signup button')
    def step_impl(self):
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()



    @then(u': User should be registered successfully')
    def step_impl(self):
        print("Registered")


