import re
from datetime import datetime


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check_integer(num):
    try:
        int(num)
    except ValueError:
        return False
    return True


def check_float(val):
    try:
        float(val)
    except ValueError:
        return False
    return True


def check_string(string):
    try:
        isinstance(string, str)
    except ValueError:
        return False
    return True


def check_email(string):
    if re.fullmatch(regex, string):
        return True
    else:
        return False


def check_datetime(Undefined):
    try:
        datetime.fromisoformat(str(Undefined))
        return True
    except ValueError:
        return False


def check_only_string(string):
    string = string.replace(" ", "")
    string = string.replace(".", "")
    if string.isalpha():
        return True
    else:
        return False
