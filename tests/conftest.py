import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium import webdriver
from demoqa_tests.utils import attach
from selenium.webdriver.chrome.options import Options


login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='Select browser to run tests',
        choices=['firefox', 'chrome'],
        default='chrome'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_name = request.config.getoption('--browser')
    options = Options()
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver

    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = '1080'
    browser.config.window_width = '1920'

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()