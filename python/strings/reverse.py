def get_reverse_string(string):
    """Reverses a string."""
    return string[::-1]


def reverse_digits(number: int) -> int:
    """Takes an int and return all digits in reversed order without leading
       zeros."""
    string_num = str(number)[::-1]  # converts to string and reverse
    string_num.lstrip("0")  # remove leading '0'
    int_reversed = int(string_num)
    return int_reversed
