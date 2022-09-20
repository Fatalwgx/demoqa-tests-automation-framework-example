from selene.support.shared import browser


def check_option(option: tuple):
    for item in option:
        browser.element(f"//label[contains(text(), '{item}')]").click()
