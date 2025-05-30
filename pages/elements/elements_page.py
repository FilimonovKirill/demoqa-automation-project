from selenium.webdriver.common.by import By
from pages.elements.text_box_page import TextBoxPage

class ElementsPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/elements"
        
    def openTextBoxSection(self):
        section_locator = self.driver.find_element(By.XPATH, f"//span[text()='Text Box']")
        section_locator.click()
        return TextBoxPage(self.driver)
        