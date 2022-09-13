from selene.support.shared import browser


def open_browser(url):
    browser.open(url)
    browser.driver.maximize_window()
