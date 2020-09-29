import datetime
import calendar


def convert_month_name_to_int(month: str) -> int:
    """Take the name of the month and map it to its integer equivalent,
    from 1 to 12."""
    month = month.lower()[:3]  # first three letters of month
    months = {v.lower(): k for k, v in enumerate(calendar.month_abbr)}
    try:
        return months[month]  # get mapping name ⇒ number
    except KeyError:
        return 0


def get_next_month_year() -> str:
    """From the current date, get the next month and return it as a string
    of the form `MMM-YYYY`."""
    today = datetime.datetime.today()
    year = today.year

    # Make sure January follows December!
    if today.month + 1 == 13:
        month = 1
        year += 1
    else:
        month = today.month + 1

    future = datetime.datetime.replace(today, month=month, year=year)
    return datetime.datetime.strftime(future, "%b-%Y")


def is_current_date_last_day_of_month() -> bool:
    """Return True if today is the last day of the month, False otherwise."""
    today = datetime.datetime.today()
    year, month, day = today.year, today.month, today.day
    return day == calendar.monthrange(year, month)
