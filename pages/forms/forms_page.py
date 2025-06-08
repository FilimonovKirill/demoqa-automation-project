import allure
from selenium.webdriver.common.by import By
from pages.forms.practice_form_page import PracticeForm

class FormsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/forms"

    @allure.step("Opening Practice Form")
    def openPracticeFormSection(self):
        section_locator = self.driver.find_element(By.XPATH, f"//span[text()='Practice Form']")
        section_locator.click()
        return PracticeForm(self.driver)
    