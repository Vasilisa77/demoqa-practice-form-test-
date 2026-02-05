import os
from selene import have, command
from selene.support.shared import browser

def test_fill_and_submit_form():
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.execute_script('document.querySelector("footer").remove()')
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Petrov')
    browser.element('#userEmail').type('ivan_test@example.com')
    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
    browser.element('#userNumber').type('9123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('May')
    browser.element('.react-datepicker__year-select').send_keys('1995')
    browser.element('.react-datepicker__day--010:not(.react-datepicker__day--outside-month)').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.all('.custom-checkbox').element_by(have.text('Sports')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('image.jpg'))
    browser.element('#currentAddress').type('Russia, Moscow, Test Street, 10')
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select-3-option]').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select-4-option]').element_by(have.exact_text('Delhi')).click()
    browser.element('#submit').press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Ivan Petrov',
            'ivan_test@example.com',
            'Male',
            '9123456789',
            '10 May,1995',
            'Computer Science',
            'Sports',
            'image.jpg',
            'Russia, Moscow, Test Street, 10',
            'NCR Delhi'
        )
    )