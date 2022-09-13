from selene.support.shared import browser
from selene import be
from demoqa_tests.utils import files
from pages.practice_page import get_nth_week_and_date_element
from pages.locators import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from demoqa_tests.model.app import open_browser


def test_submit_filled_form():
    open_browser(PRACTICE_PAGE)
    browser.element(FIRST_NAME).type('TestName')
    browser.element(LAST_NAME).type('TestLastName')
    browser.element(EMAIL).type('123@mail.ru')
    browser.element(GENDER_MALE).click()
    browser.element(PHONE).type('70000000000')
    browser.element(DATE_OF_BIRTH).click()
    Select(browser.find_element(By.CSS_SELECTOR, 'select.react-datepicker__month-select')).select_by_value(
        '6')
    Select(browser.find_element(By.CSS_SELECTOR, 'select.react-datepicker__year-select')).select_by_value(
        '1997')
    get_nth_week_and_date_element('5', '29').click()
    browser.element(SUBJECTS).type('Computer Science').press_enter()
    browser.element(SUBJECTS).type('English').press_enter()
    browser.element(HOBBIES_READING).click()
    browser.element(HOBBIES_MUSIC).click()
    browser.element(UPLOAD_PICTURE).send_keys(files.path_to_test_picture('../resources/picture.png'))
    browser.element(ADDRESS_CURRENT).type('some address')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.element(STATE).click()
    browser.element(STATE_OPTION_NCR).click()
    browser.element(CITY).click()
    browser.element(CITY_NCR_DELHI).click()
    browser.element(SUBMIT_BUTTON).click()
    browser.element(MODAL_BODY).should(be.visible)
