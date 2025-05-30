from faker import Faker
from pages.main_page import MainPage
from constants.objects.user import User
    
def generate_user():
    fake = Faker()
    return User(
        first_name=fake.first_name_male(),
        last_name=fake.last_name_male(),
        email=fake.email(),
        gender="Male",
        mobile_number="1234567890",
        birth_date= f"{fake.day_of_month()} {fake.month_name()} {fake.year()}",
        hobbies=["Sports", "Music"],
        current_address="address",
    )
    
def test_main_to_practice_form(driver):
    user = generate_user()
    
    forms_page = MainPage(driver).open().openFormsSection()
    
    practice_form_page = forms_page.openPracticeFormSection()
    
    practice_form_page \
        .input_first_name(user.first_name) \
        .input_last_name(user.last_name) \
        .input_email(user.email) \
        .choose_gender(user.gender) \
        .input_mobile_number(user.mobile_number) \
        .pick_birth_date(user.birth_date) \
        .choose_hobbies(user.hobbies) \
        .input_current_address(user.current_address) \
        .click_submit() \
        .check_full_name(f"{user.first_name} {user.last_name}") \
        .check_email(user.email) \
        .check_mobile(user.mobile_number) \
        .check_birth_date(user.birth_date) \
        .check_hobbies(user.hobbies) \
        .check_address(user.current_address)