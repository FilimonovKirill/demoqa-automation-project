import allure
from selenium.webdriver.common.by import By
from pages.elements.elements_page import ElementsPage
from pages.forms.forms_page import FormsPage

class MainPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/"

    @allure.step("Opening demoqa main page")
    def open(self):
        self.driver.get(self.url)
        return self

    @allure.step("Opening Elements page")
    def openElementsSection(self):
        section_locator = self.driver.find_element(By.XPATH, "//h5[text()='Elements']")
        section_locator.click()
        return ElementsPage(self.driver)

    @allure.step("Opening Forms page")
    def openFormsSection(self):
        section_locator = self.driver.find_element(By.XPATH, "//h5[text()='Forms']")
        section_locator.click()
        return FormsPage(self.driver)
    