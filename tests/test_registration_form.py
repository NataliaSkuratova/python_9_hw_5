from selene import browser, have, be, by
import os


def test_registration_form():
    browser.open('/')
    browser.element('.main-header').should(have.text('Practice Form'))
    browser.element('#firstName').should(be.blank).type('Natalia')
    browser.element('#lastName').should(be.blank).type('Skuratova')
    browser.element('#userEmail').should(be.blank).type('aabc@gmail.com')
    browser.element("[for='gender-radio-2']").click()
    browser.element('#userNumber').type('6575755765')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().type('December').click()
    browser.element('.react-datepicker__year-select').click().type('1987').click()
    browser.element('.react-datepicker__day--026').click()
    browser.element("#subjectsInput").set_value("Chemistry").press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('pictures/rubiks_cube.jpg'))
    browser.element('#currentAddress').type('Moscow, Park street, 88')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').press_enter()
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.all("tbody tr td:last-child").should(have.exact_texts(
        'Natalia Skuratova', 'aabc@gmail.com', 'Female',
        '6575755765', '26 December,1987', 'Chemistry',
        'Sports', 'rubiks_cube.jpg',
        'Moscow, Park street, 88', 'Haryana Karnal'))
    browser.element('#closeLargeModal').press_enter()
