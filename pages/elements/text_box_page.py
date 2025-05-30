from selenium.webdriver.common.by import By
from utils.helpers import assert_element_text
from utils.helpers import type_text

class TextBoxPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/text-box"
        
    def input_full_name(self, full_name):
        full_name_input = self.driver.find_element(By.ID, "userName")
        type_text(full_name_input, full_name)
        return self
        
    def input_email(self, email):
        email_input = self.driver.find_element(By.ID, "userEmail")
        type_text(email_input, email)
        return self
        
    def input_current_address(self, current_address):
        current_address_input = self.driver.find_element(By.ID, "currentAddress")
        type_text(current_address_input, current_address)
        return self
        
    def input_permanent_address(self, permanent_address):
        permanent_address_input = self.driver.find_element(By.ID, "permanentAddress")
        type_text(permanent_address_input, permanent_address)
        return self
    
    def submitForm(self):
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()
        return self
        
    def check_full_name(self, full_name):
        locator = (By.ID, "name")
        expected_text = f"Name:{full_name}"
        assert_element_text(self.driver, locator, expected_text)
        return self

    def check_email(self, email):
        locator = (By.ID, "email")
        expected_text = f"Email:{email}"
        assert_element_text(self.driver, locator, expected_text)
        return self

    def check_current_address(self, current_address):
        locator = (By.XPATH, "//p[@id='currentAddress']")
        expected_text = f"Current Address :{current_address}"
        assert_element_text(self.driver, locator, expected_text)
        return self

    def check_permanent_address(self, permanent_address):
        locator = (By.XPATH, "//p[@id='permanentAddress']")
        expected_text = f"Permananet Address :{permanent_address}"
        assert_element_text(self.driver, locator, expected_text)
        return self
    