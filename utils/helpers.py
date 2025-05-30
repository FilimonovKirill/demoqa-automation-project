from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def assert_element_text(driver, locator, expected_text, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
    print(element.text)
    assert element.text == expected_text, f"Ожидалось: '{expected_text}', но найдено: '{element.text}'"
    
def type_text(locator, text):
    locator.clear()
    locator.send_keys(text)
    
def pick_date(driver, date_input_locator, date_str, timeout=10):
    date_input = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(date_input_locator)
    )
    date_input.click()

    day, month, year = date_str.split()

    year_dropdown = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__year-select"))
    )
    year_dropdown.click()
    year_dropdown.find_element(By.XPATH, f".//option[text()='{year}']").click()

    month_dropdown = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    month_dropdown.click()
    month_dropdown.find_element(By.XPATH, f".//option[text()='{month}']").click()

    day_cell = driver.find_element(
        By.XPATH,
        f"//div[contains(@class, 'react-datepicker__day') and text()='{int(day)}' and not(contains(@class, 'outside-month'))]"
    )
    day_cell.click()
    
def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)