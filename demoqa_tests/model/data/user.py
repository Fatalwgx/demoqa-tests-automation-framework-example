from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Tuple, Literal

import demoqa_tests


class Gender(Enum):
    Male = 1
    Female = 2
    Other = 3


class Hobby(Enum):
    Music = 'Music'
    Reading = 'Reading'
    Sports = 'Sports'


class Subjects(Enum):
    Math = 'Math'
    English = 'English'
    Computer_science = 'Computer Science'


def format_date(value: datetime.date):
    return value.strftime(demoqa_tests.config.datetime_format)
