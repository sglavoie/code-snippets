from math import sqrt


def triangle_type(side_a, side_b, side_c) -> str:
    """Return a string telling the type of triangle based on its
    sides."""
    theoretical_hypotenuse = sqrt(side_a ** 2 + side_b ** 2)
    if side_c == theoretical_hypotenuse:
        return "R"  # if Pythagorean Theorem works, it is a right triangle

    if side_c < theoretical_hypotenuse:
        return "A"  # acute triangle

    return "O"  # obtuse triangle
