def bin_converter(number):
    """Recursive implementation to convert number in base 10 to base 2.

    Could also use built-in function bin(), but that wouldn't be a
    challenge, right? It doesn't mention how it has to be done..."""
    # Base cases to avoid entering into an infinite recursion loop
    if number == 1:
        return 1
    if number == 0:
        return 0

    next_num = number // 2
    remainder = number % 2

    # The last remainder goes first, so the return statement begins with
    # the recursive call.
    return "{}".format(bin_converter(next_num)) + "{}".format(remainder)


def convert_integer_to_bin_number(num):
    return int(bin(num)[2:])


def consecutive_ones(str_number):
    """Returns the maximum number of times a consecutive '1' appears in
    NUMBER, which is a string in this scenario."""
    maximum, current = 0, 0
    for num in str_number:
        if num == "1":
            current += 1
        else:
            maximum = max(maximum, current)
            current = 0

    return max(maximum, current)


def count_bits(bin_string):
    """Return the number of bits in a string of zeros and ones."""
    counter = 0
    for char in bin_string:
        if char == "1":
            counter += 1
    return counter


def convert_string_to_bin_number(string_int):
    return bin(int(string_int))[2:]
