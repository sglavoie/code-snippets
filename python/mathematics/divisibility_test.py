def test_digit_division(number: int) -> dict:
    """Test divisibility of number from 2 to 9."""
    digit_division = {}
    for digit in range(2, 10):
        if number % digit == 0:
            digit_division[digit] = True
        else:
            digit_division[digit] = False
    return digit_division
