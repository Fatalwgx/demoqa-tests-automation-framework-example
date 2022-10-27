import datetime

from selene import have

import demoqa_tests


def date(value: datetime.date):
    return have.value(value.strftime(demoqa_tests.config.datetime_format))
