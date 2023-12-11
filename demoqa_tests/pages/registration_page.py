from selene import browser, be, have, command

from demoqa_tests import resource
from demoqa_tests.data.users import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).with_(type_by_js=True).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).with_(type_by_js=True).type(value)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).with_(type_by_js=True).type(value)

    def check_box_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def fill_phone_number(self, value):
        browser.element('#userNumber').should(be.blank).with_(type_by_js=True).type(value)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def pick_subjects(self, subject1, subject2):
        browser.element('#subjectsContainer').click()
        browser.element('#subjectsInput').type(subject1).press_enter()
        browser.element('#subjectsInput').type(subject2).press_enter()

    def check_box_hobbies(self, hobbie1, hobbie2, hobbie3):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobbie1)).click()
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobbie2)).click()
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobbie3)).click()

    def upload_picture(self, value):
        browser.element("#uploadPicture").set_value(resource.path(value))

    def fill_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).with_(type_by_js=True).type(value)

    def pick_state_and_city(self, state, city):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(city)).click()

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.check_box_gender(user.gender)
        self.fill_phone_number(user.phone_number)
        self.fill_date_of_birth(user.day_of_birth, user.month_of_birth, user.year_of_birth)
        self.pick_subjects(user.subjects[0], user.subjects[1])
        self.check_box_hobbies(user.hobbies[0], user.hobbies[1], user.hobbies[2])
        self.upload_picture(user.picture)
        self.fill_current_address(user.current_address)
        self.pick_state_and_city(user.state, user.city)
        self.submit_form()

    def assert_user_info(
            self, full_name, email, gender, phone_number, date_of_birth, subjects, hobbies,
            picture, current_address, city_and_state
    ):
        browser.element('.table').all('td:last-child').should(have.exact_texts(
            full_name, email, gender, phone_number, date_of_birth, subjects, hobbies,
            picture, current_address, city_and_state)
        )

    def close_modal_window(self):
        browser.element('#closeLargeModal').perform(command.js.scroll_into_view).click()
