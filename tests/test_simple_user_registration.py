from selene import browser, have, command


def test_simple_registration():
    browser.open('/text-box')

    browser.element('#userName').type('Sergey Dobrovolskiy')
    browser.element('#userEmail').type('svdobrovolskiy@qa.ru')
    browser.element('#currentAddress').type('Marshaka 5')
    browser.element('#permanentAddress').type('Nikitinskaya 9')
    browser.element('#submit').click()

    browser.element('#output').perform(command.js.scroll_into_view)
    browser.element('#output #name').should(have.exact_text('Name:Sergey Dobrovolskiy'))
    browser.element('#output #email').should(have.exact_text('Email:svdobrovolskiy@qa.ru'))
    browser.element('#output #currentAddress').should(have.exact_text('Current Address :Marshaka 5'))
    browser.element('#output #permanentAddress').should(have.exact_text('Permananet Address :Nikitinskaya 9'))