import re


def is_valid_regex(regex_expr):
    try:
        re.search(regex_expr, 'string')
        return True
    except re.error:
        return False
