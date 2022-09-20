from selenium.webdriver.common.keys import Keys
from selene.support.shared import browser


def set_date(date: str):
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL + 'a' + Keys.NULL, date).press_enter()
