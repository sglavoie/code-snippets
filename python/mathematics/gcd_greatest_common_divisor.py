def gcd(a, b):
    """Returns the greatest common divisor between "a" and "b"."""
    if a == b:
        return a
    else:
        if a > b:
            return gcd(a - b, b)
        elif a < b:
            return gcd(a, b - a)


def gcd_recursive(a, b):
    """
    a, b: positive integers

    Returns: a positive integer, the greatest common divisor of a & b.
    """
    big_int = max([a, b])
    small_int = min([a, b])
    if big_int % small_int == 0:
        return small_int
    else:
        return gcd_recursive(small_int, big_int % small_int)


def gcd_iterative(a, b):
    """
    a, b: positive integers

    Returns: a positive integer, the greatest common divisor of a & b.
    """
    big_int = max([a, b])
    small_int = min([a, b])
    while small_int > 1:
        if big_int % small_int == 0 and min([a, b]) % small_int == 0:
            return small_int
        small_int -= 1

    return 1
