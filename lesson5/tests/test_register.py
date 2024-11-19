from faker import Faker
fake = Faker()
def test_register_as_tutor(header, register):
    header.visit()
    header.click_on_registration_button()
    register.should_be_opened()
    register.fill_nick(fake.user_name())
    register.fill_password("Password098*")
    register.fill_confirm_password("Password098*")
    register.click_on_become_a_teacher_button()
    register.click_on_registration_button()
    header.create_listing_button_should_be_visible()