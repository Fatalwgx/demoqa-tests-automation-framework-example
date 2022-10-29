import datetime
import time

from demoqa_tests.model import app
from demoqa_tests.model.data import user
from demoqa_tests.model.data.user import Gender
from demoqa_tests.model.pages import practice_page


def test_submit_filled_form():

    # GIVEN
    app.given_opened('/automation-practice-form')

    # WHEN
    practice_page.fill_fullname('Lev', 'Zavodskov')
    practice_page.fill_email('email@example.com')
    practice_page.fill_gender(Gender.Male)
    practice_page.fill_phone('70000000000')
    practice_page.fill_birthday(datetime.date(1997, 7, 29))
    practice_page.fill_subjects(user.Subjects.Math, user.Subjects.English, user.Subjects.Computer_science)
    practice_page.fill_hobbies(user.Hobby.Music, user.Hobby.Reading)
    practice_page.select_picture('picture.png')
    practice_page.fill_address('Country/State/City/Street/ Street num')
    practice_page.select_state('NCR')
    practice_page.select_city('Gurgaon')
    practice_page.submit_form()

    # THEN
    practice_page.assert_form_sent()
