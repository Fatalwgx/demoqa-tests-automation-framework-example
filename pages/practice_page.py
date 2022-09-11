from pages.base_page import BasePage
from pages.locators import PracticePageLocators
from selene.support.shared import browser


class PracticePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url


    def get_nth_week_and_date_element(self, week: str, date: str):
        return self.browser.element(f'.react-datepicker__week:nth-child({week}) [class="react-datepicker__day react-datepicker__day--0{date}"]')