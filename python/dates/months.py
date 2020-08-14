import calendar


def convert_month_name_to_int(month: str) -> int:
    month = month.lower()[:3]  # first three letters of month
    months = {v.lower(): k for k, v in enumerate(calendar.month_abbr)}
    try:
        return months[month]  # get mapping name ⇒ number
    except KeyError:
        return 0
