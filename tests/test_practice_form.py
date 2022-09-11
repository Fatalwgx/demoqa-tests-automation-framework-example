from selene.support.shared import browser
from selene import have, be
from utils import files
from pages.practice_page import PracticePage
from pages.locators import PracticePageLocators
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time



def open_practice_form():
    browser.open(PracticePageLocators.LINK)
    browser.driver.maximize_window()


def test_submit_filled_form():
    page = PracticePage(browser, PracticePageLocators.LINK)
    open_practice_form()
    browser.element(PracticePageLocators.FIRST_NAME).type('TestName')
    browser.element(PracticePageLocators.LAST_NAME).type('TestLastName')
    browser.element(PracticePageLocators.EMAIL).type('123@mail.ru')
    browser.element(PracticePageLocators.GENDER_MALE).click()
    browser.element(PracticePageLocators.PHONE).type('70000000000')
    browser.element(PracticePageLocators.DATE_OF_BIRTH).click()
    Select(browser.find_element(By.CSS_SELECTOR, 'select.react-datepicker__month-select')).select_by_value(
        '6')
    Select(browser.find_element(By.CSS_SELECTOR, 'select.react-datepicker__year-select')).select_by_value(
        '1997')
    page.get_nth_week_and_date_element('5', '29').click()
    browser.element(PracticePageLocators.SUBJECTS).type('Computer Science').press_enter()
    browser.element(PracticePageLocators.SUBJECTS).type('English').press_enter()
    browser.element(PracticePageLocators.HOBBIES_READING).click()
    browser.element(PracticePageLocators.HOBBIES_MUSIC).click()
    browser.element(PracticePageLocators.UPLOAD_PICTURE).send_keys(files.path_to_test_picture('../utils/picture.png'))
    browser.element(PracticePageLocators.ADDRESS_CURRENT).type('some address')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.element(PracticePageLocators.STATE).click()
    browser.element(PracticePageLocators.STATE_OPTION_NCR).click()
    browser.element(PracticePageLocators.CITY).click()
    browser.element(PracticePageLocators.CITY_NCR_DELHI).click()
    browser.element(PracticePageLocators.SUBMIT_BUTTON).click()
    browser.element(PracticePageLocators.MODAL_BODY).should(be.visible)
