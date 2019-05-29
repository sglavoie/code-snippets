def factorial(number):
    """n! = n * (n-1)!
    4! = 4 * 3! = 4 * 3 * 2! = 4 * 3 * 2 * 1! = 4 * 3 * 2 * 1"""

    if number == 1:  # Define base case → n = 1
        return 1
    # Define recursive case
    return number * factorial(number - 1)
