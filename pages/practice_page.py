from selene.support.shared import browser


def get_nth_week_and_date_element(week: str, date: str):
    return browser.element(f'.react-datepicker__week:nth-child({week}) [class="react-datepicker__day react-datepicker__day--0{date}"]')