def gcd(a, b):
    """Returns the greatest common divisor between "a" and "b"."""
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)


def lcm(a, b):
    """Returns the least common multiple between "a" and "b"."""
    return a * b / gcd(a, b)
