def is_this_prime(number):
    if number <= 3:
        return number > 1  # True if 2 or 3

    if number % 2 == 0 or number % 3 == 0:
        return False  # False if divisible by 2 or 3

    num = 5
    while num ** 2 <= number:  # Check up to sqrt(number)
        if number % num == 0 or number % (num + 2) == 0:
            return False
        num = num + 6
    return True
