from selene import browser, have, command


class SimpleRegistrationPage:

    def open(self):
        browser.open('/text-box')

    def fill_full_name(self, value):
        browser.element('#userName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_permanent_address(self, value):
        browser.element('#permanentAddress').type(value)

    def submit(self):
        browser.element('#submit').click()


def test_simple_registration():
    simple_registration_page = SimpleRegistrationPage()

    simple_registration_page.open()

    simple_registration_page.fill_full_name('Sergey Dobrovolskiy')
    simple_registration_page.fill_email('svdobrovolskiy@qa.ru')
    simple_registration_page.fill_current_address('Marshaka 5')
    simple_registration_page.fill_permanent_address('Nikitinskaya 9')
    simple_registration_page.submit()

    browser.element('#output #name').perform(command.js.scroll_into_view).should(have.exact_text('Name:Sergey Dobrovolskiy'))
    browser.element('#output #email').should(have.exact_text('Email:svdobrovolskiy@qa.ru'))
    browser.element('#output #currentAddress').should(have.exact_text('Current Address :Marshaka 5'))
    browser.element('#output #permanentAddress').should(have.exact_text('Permananet Address :Nikitinskaya 9'))