from selenium.webdriver.common.by import By
from utils.helpers import type_text
from utils.helpers import pick_date
from utils.helpers import assert_element_text
from utils.helpers import scroll_to_element

class PracticeForm:
    
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"

    def input_first_name(self, first_name):
        first_name_input = self.driver.find_element(By.ID, "firstName")
        type_text(first_name_input, first_name)
        return self
    
    def input_last_name(self, last_name):
        last_name_input = self.driver.find_element(By.ID, "lastName")
        type_text(last_name_input, last_name)
        return self
    
    def input_email(self, email):
        email_input = self.driver.find_element(By.ID, "userEmail")
        type_text(email_input, email)
        return self
    
    def choose_gender(self, gender):
        gender_button = self.driver.find_element(By.XPATH, f"//input[@value='{gender}']/following-sibling::label")
        gender_button.click()
        return self
    
    def input_mobile_number(self, mobile_number):
        mobile_number_input = self.driver.find_element(By.ID, "userNumber")
        type_text(mobile_number_input, mobile_number)
        return self
    
    def pick_birth_date(self, date_str):
        pick_date(self.driver, (By.ID, "dateOfBirthInput"), date_str)
        return self
            
    def choose_hobbies(self, hobbies: list[str]):
        for hobby in hobbies:
            label = self.driver.find_element(By.XPATH, f"//label[contains(., '{hobby}')]")
            label.click()
        return self
    
    def input_current_address(self, address):
        address_input = self.driver.find_element(By.ID, "currentAddress")
        type_text(address_input, address)
        return self
    
    def click_submit(self):
        submit_button = self.driver.find_element(By.ID, "submit")
        scroll_to_element(self.driver, submit_button)
        submit_button.click()
        return self
    
    def check_full_name(self, expected):
        locator = (By.XPATH, "//td[text()='Student Name']/following-sibling::td")
        assert_element_text(self.driver, locator, expected)
        return self

    def check_email(self, expected):
        locator = (By.XPATH, "//td[text()='Student Email']/following-sibling::td")
        assert_element_text(self.driver, locator, expected)
        return self

    def check_gender(self, expected):
        locator = (By.XPATH, "//td[text()='Gender']/following-sibling::td")
        assert_element_text(self.driver, locator, expected)
        return self

    def check_mobile(self, expected):
        locator = (By.XPATH, "//td[text()='Mobile']/following-sibling::td")
        assert_element_text(self.driver, locator, expected)
        return self

    def check_birth_date(self, expected):
        parts = expected.split(" ")
        expected = f"{parts[0]} {parts[1]},{parts[2]}"
        locator = (By.XPATH, "//td[text()='Date of Birth']/following-sibling::td")
        assert_element_text(self.driver, locator, expected)
        return self

    def check_hobbies(self, expected: list[str]):
        locator = (By.XPATH, "//td[text()='Hobbies']/following-sibling::td")
        assert_element_text(self.driver, locator, ", ".join(expected))
        return self

    def check_address(self, expected):
        locator = (By.XPATH, "//td[text()='Address']/following-sibling::td")
        assert_element_text(self.driver, locator, expected)
        return self
