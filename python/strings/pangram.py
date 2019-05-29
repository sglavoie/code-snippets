import string


def is_pangram(user_str):
    alpha_str = set()
    for char in user_str.lower():
        if char in string.ascii_lowercase and char not in alpha_str:
            alpha_str.add(char)
            if len(alpha_str) == 26:
                return "pangram"
    return "not pangram"
