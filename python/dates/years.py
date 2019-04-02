def is_julian_leap(year: int) -> bool:
    return year % 4 == 0


def is_gregorian_leap(year: int) -> bool:
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0
