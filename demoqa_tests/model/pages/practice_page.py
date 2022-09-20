from selene.support.shared import browser
from demoqa_tests.model.controls import dropdown
from selene import be


def fill_fullname(firstname: str, lastname: str):
    browser.element('#firstName').type(firstname)
    browser.element('#lastName').type(lastname)


def fill_phone(phone: str):
    browser.element('#userNumber').type(phone)


def fill_subjects(subjects: tuple):
    for item in subjects:
        browser.element('#subjectsInput').type(item).press_enter().press_escape()


def fill_address(address):
    browser.element('#currentAddress').type(address)


def select_state(state: str):
    element = browser.element('#state')
    dropdown.select(element, state)


def select_city(city: str):
    element = browser.element('#city')
    dropdown.select(element, city)


def submit_form():
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.element('#submit').click()


def assert_form_sent():
    browser.element('.modal-body').should(be.visible)
