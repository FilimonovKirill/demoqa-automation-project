from faker import Faker
from pages.main_page import MainPage
from constants.objects.user import User
    
def generate_user():
    fake = Faker()
    return User(
        first_name=fake.first_name_male(),
        last_name=fake.last_name_male(),
        email=fake.email(),
        current_address="address",
    )
    
def test_main_to_text_box(driver):
    user = generate_user()
    
    main_page = MainPage(driver)
    main_page.open()
    
    elements_page = main_page.openElementsSection()
    text_box_page = elements_page.openTextBoxSection()
    
    text_box_page \
        .input_full_name(user.full_name) \
        .input_email(user.email) \
        .input_current_address(user.current_address) \
        .input_permanent_address(user.permanent_address) \
        .submitForm() \
        .check_full_name(user.full_name) \
        .check_email(user.email) \
        .check_current_address(user.current_address) \
        .check_permanent_address(user.permanent_address)