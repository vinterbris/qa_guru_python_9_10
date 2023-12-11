from selene import have
from demoqa_tests.pages.registration_page import RegistrationPage


def test_registration():
    registration_page = RegistrationPage()
    registration_page.open()
    # WHEN
    registration_page.fill_first_name('Sergey')
    registration_page.fill_last_name('Dobrovolskiy')
    registration_page.fill_email('dobrovolskiy@qa.ru')
    registration_page.check_box_gender('Male')
    registration_page.fill_phone_number('1002003040')
    registration_page.fill_date_of_birth('02', 'January', '2100')
    registration_page.pick_subjects('Maths', 'Chemistry')
    registration_page.check_box_hobbies('Sports', 'Reading', 'Music')
    registration_page.upload_picture('nolan.jpg')
    registration_page.fill_current_address('Test Address')
    registration_page.pick_state_and_city('NCR', 'Delhi')
    registration_page.submit_form()

    # THEN
    registration_page.registered_user_data.should(have.exact_texts(
        'Sergey Dobrovolskiy', 'dobrovolskiy@qa.ru', 'Male', '1002003040', '02 January,2100',
        'Maths, Chemistry', 'Sports, Reading, Music', 'nolan.jpg', 'Test Address', 'NCR Delhi')
    )
    registration_page.close_modal_window()
