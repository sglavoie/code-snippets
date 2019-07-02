def is_julian_leap(year: int) -> bool:
    """Return whether a year is leap in a Julian calendar as a boolean."""
    return year % 4 == 0


def is_gregorian_leap(year: int) -> bool:
    """Return whether a year is leap in a Gregorian calendar as a boolean."""
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0
