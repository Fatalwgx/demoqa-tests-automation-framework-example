from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selene import have, command


def given_opened(url):
    browser.open(url)
    ads = ss('[id^=google_ads][id$=container__]')
    if ads.with_(timeout=15).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)
