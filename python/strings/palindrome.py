def is_palindrome(string) -> bool:
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and is_palindrome(string[1:-1])
