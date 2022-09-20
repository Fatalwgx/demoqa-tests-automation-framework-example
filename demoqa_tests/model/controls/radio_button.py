from selene.support.shared import browser


def set_option(option_num: int):
    browser.element(f'[for=gender-radio-{option_num}]').click()