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
    browser.element('#subjectsInput').should(be.blank).type('inform').click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('pictures/rubiks_cube.jpg'))
    browser.element('#currentAddress').type('Moscow, Park street, 88')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text(
        'Natalia Skuratova' and
        'aabc@gmail.com' and
        'Female' and
        '6575755765' and
        '26 december, 1987' and
        'inform' and
        'Sports' and
        'rubiks_cube.jpeg' and
        'moscow, park street, 88' and
        'Hayana' and
        'Karnal'
    ))
    browser.element('#closeLargeModal').press_enter()
