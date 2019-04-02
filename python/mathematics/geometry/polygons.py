import math


def poly_sum(n, s):
    """Calculates the area of a regular polygon, then calculates the
    square of its perimeter and returns the sum of both calculations.

    Arguments:
    'n' corresponds to the number of sides of the regular polygon.
    's' corresponds to the length of every side of that polygon.
    """
    area = 0.25 * n * s ** 2 / math.tan(math.pi / n)
    perimeter_squared = (n * s) ** 2
    sum_polysum = area + perimeter_squared

    return round(sum_polysum, 4)
