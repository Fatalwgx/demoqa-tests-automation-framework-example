import os

import pytest
from selene.support.shared import browser

from demoqa_tests.utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = 'chrome'
    browser.config.window_height = '1080'
    browser.config.window_width = '1920'
    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
