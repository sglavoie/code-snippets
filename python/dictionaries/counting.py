def dict_count(arr: list) -> dict:
    """Count the number of occurrences for each value in the array and return
       a dictionary where keys are the elements in the array and values are
       the number of times each element appears in the array."""
    arr_dict = {}
    for value in arr:
        if value in arr_dict:
            arr_dict[value] += 1
        else:
            arr_dict[value] = 1
    return arr_dict


def count_of_digits(number: int) -> dict:
    '''Return a dictionary with digits from 1 to 9 as keys and indicate the
       number of times each digit appear for each key in number.'''
    number_string = str(number)
    digit_dict = {}
    for digit in range(1, 10):
        count_digit = number_string.count(str(digit))
        digit_dict[digit] = count_digit
    return digit_dict
