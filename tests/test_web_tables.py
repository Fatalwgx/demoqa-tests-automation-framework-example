"""from selene.support.shared import browser
from selene import have
from demoqa_tests.model.app import open_browser
from demoqa_tests.model.pages.web_tables_page import get_row_group
from demoqa_tests.model.pages.web_tables_page import edit_row
from demoqa_tests.model.pages.web_tables_page import delete_row


def test_webtable_operations():
    open_browser(WEB_TABLES_PAGE)
    browser.element(BUTTON_ADD).click()
    browser.element(FIRST_NAME).type('Lev')
    browser.element(LAST_NAME).type('Zavodskov')
    browser.element(EMAIL).type('123@mail.ru')
    browser.element(AGE).type('25')
    browser.element(SALARY).type('9999999999')
    browser.element(DEPARTMENT).type('SDET?')
    browser.element(SUBMIT_BUTTON).click()
    browser.element(edit_row(2)).click()
    browser.element(FIRST_NAME).set_value('nedlA')
    browser.element(LAST_NAME).set_value('llertnaC')
    browser.element(EMAIL).set_value('nedlA@elpmaxe.moc')
    browser.element(AGE).set_value('54')
    browser.element(SALARY).set_value('00021')
    browser.element(DEPARTMENT).set_value('ecnailpmoC')
    browser.element(SUBMIT_BUTTON).click()
    browser.element(delete_row(3)).click()
    browser.element(get_row_group(3) + ' .rt-td:nth-child(1)').should(have.text('Lev'))
"""