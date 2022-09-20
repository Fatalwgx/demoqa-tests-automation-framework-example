from demoqa_tests.model.app import given_opened_browser
from demoqa_tests.model.pages.practice_page import *
from demoqa_tests.model.controls import datepicker, radio_button, checkbox, file_attribute


def test_submit_filled_form():
    # GIVEN
    given_opened_browser('/automation-practice-form')
    #WHEN
    fill_fullname('Lev', 'Zavodskov')
    radio_button.set_option(1)
    fill_phone('70000000000')
    datepicker.set_date('29 Jul 1997')
    fill_subjects(('Math', 'English', 'Computer Science'))
    checkbox.check_option(('Music', 'Reading'))
    file_attribute.upload('../resources/picture.png')
    fill_address('Country/State/City/Street/ Street num')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    select_state('NCR')
    select_city('Gurgaon')
    submit_form()
    #THEN
    assert_form_sent()
