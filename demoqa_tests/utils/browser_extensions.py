from selene import command
from selene.support.shared import browser

from demoqa_tests.utils.selene import action


def scroll_one_page():
    browser.perform(action.js.scroll_one_page)
