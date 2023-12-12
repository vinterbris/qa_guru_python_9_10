from demoqa_tests.application import app
from demoqa_tests.pages.simple_registration_page import SimpleRegistrationPage


def test_simple_registration():
    app.left_panel.open_simple_registration_form()

    app.simple_registration.open()
    app.simple_registration.fill_full_name('Sergey Dobrovolskiy')
    app.simple_registration.fill_email('svdobrovolskiy@qa.ru')
    app.simple_registration.fill_current_address('Marshaka 5')
    app.simple_registration.fill_permanent_address('Nikitinskaya 9')
    app.simple_registration.submit()

    app.simple_registration.should_have_registered_user_info('Name:Sergey Dobrovolskiy',
                                                              'Email:svdobrovolskiy@qa.ru',
                                                              'Current Address :Marshaka 5',
                                                              'Permananet Address :Nikitinskaya 9')
