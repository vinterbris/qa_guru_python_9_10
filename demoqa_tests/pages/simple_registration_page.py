from selene import browser, command, have


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

    def should_have_registered_user_info(self, full_name, email, current_address, permanent_address):
        browser.element('#output #name').perform(command.js.scroll_into_view).should(have.exact_text(full_name))
        browser.element('#output #email').should(have.exact_text(email))
        browser.element('#output #currentAddress').should(have.exact_text(current_address))
        browser.element('#output #permanentAddress').should(have.exact_text(permanent_address))
