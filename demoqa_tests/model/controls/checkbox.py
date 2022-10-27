from selene import have
from selene.support.shared import browser


def check_options(elements, *options: str):
    for option in options:
        elements.by(have.exact_text(option)).first.element('..').click()
