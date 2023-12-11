from selene import have

from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import RegistrationPage


def test_registration():
    registration_page = RegistrationPage()
    registration_page.open()
    # WHEN
    registration_page.register(users.student)

    # THEN
    registration_page.assert_user_info(
        'Sergey Dobrovolskiy', 'dobrovolskiy@qa.ru', 'Male', '1002003040',
        '02 January,2100', 'Maths, Chemistry', 'Sports, Reading, Music', 'nolan.jpg',
        'Test Address', 'NCR Delhi'
    )
    registration_page.close_modal_window()
