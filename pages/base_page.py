from selene.support.shared import browser

class BasePage:
    def __init__(self, driver, url, *args, **kwargs):
        self.driver = driver
        self.url = url

    def open_browser(self, url, *args, **kwargs):
        browser.open(url)
