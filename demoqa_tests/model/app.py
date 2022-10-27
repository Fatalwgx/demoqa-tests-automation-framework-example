from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
from selene import have

from demoqa_tests.utils.selene import action


def given_opened(url):
    browser.open(url)
    ads = ss('[id^=google_ads][id$=container__]')
    if ads.with_(timeout=10).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(action.js.remove)
