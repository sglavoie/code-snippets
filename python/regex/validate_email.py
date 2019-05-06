import re


def validate_email(email_addr):
    pattern = r"[a-z]+[a-z0-9]*[\w._-]*@[a-z]+\.[a-z]{1,3}$"
    return re.match(pattern, email_addr)
