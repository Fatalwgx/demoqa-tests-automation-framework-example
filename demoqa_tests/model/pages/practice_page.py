import datetime

from selene.support.shared import browser

from demoqa_tests import utils
from demoqa_tests.model.controls import dropdown, radio_button, datepicker, checkbox, tags_input
from selene import be, command

from demoqa_tests.utils import files
from demoqa_tests.utils.selene.conditions import match
from demoqa_tests.model.data import user


birthday = browser.element('#dateOfBirthInput')


def fill_fullname(firstname: str, lastname: str):
    browser.element('#firstName').type(firstname)
    browser.element('#lastName').type(lastname)


def fill_email(address: str):
    browser.element('#userEmail').type(address)


def fill_phone(phone: str):
    browser.element('#userNumber').type(phone)


def fill_subjects(*subjects: user.Subjects):
    tags_input.add(browser.element('#subjectsInput'), *[subject.value for subject in subjects])


def fill_address(address):
    browser.element('#currentAddress').type(address)


def select_state(state: str):
    utils.browser_extensions.scroll_one_page()
    dropdown.select(browser.element('#state'), state)


def select_city(city: str):
    utils.browser_extensions.scroll_one_page()
    dropdown.select(browser.element('#city'), city)


def submit_form():
    utils.browser_extensions.scroll_one_page()
    browser.element('#submit').perform(command.js.click)


def assert_form_sent():
    browser.element('.modal-body').should(be.visible)


def fill_gender(value: user.Gender):
    radio_button.set_option('gender', value.value)   # noqa


def fill_birthday(date: datetime.date):
    datepicker.set_date(birthday, date)


def assert_filled_birthday(date: datetime.date):
    birthday.should(match.date(date))


def fill_hobbies(*options: user.Hobby):
    checkbox.check_options(
        browser.all('[for^=hobbies-checkbox]'), *[option.value for option in options]
    )


def select_picture(file_name):
    browser.element('#uploadPicture').send_keys(files.to_resource(f'{file_name}'))
