import datetime

import selene
from selenium.webdriver.common.keys import Keys
from demoqa_tests.model.data import user


def set_date(element: selene.Element, date: datetime.date):
    element.send_keys(
        Keys.CONTROL + 'a' + Keys.NULL,
        user.format_date(date),
    ).press_enter()


# Example of assertions built in pageobject
# def assert_value(element: selene.Element, date: datetime.date):
#    element.should(have.value(user.format_date(date)))
