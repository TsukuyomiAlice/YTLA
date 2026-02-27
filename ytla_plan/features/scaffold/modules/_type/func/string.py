# encode = utf-8

def first_letter_upper(s):
    """
    Switch a word's first letter into uppercase.
    :param s: The string to switch to.
    :return: The string with uppercase.
    """
    if s:
        return s[0].upper() + s[1:]
    return s


def first_letter_lower(s):
    """
    Switch a word's first letter into lowercase.
    :param s: The string to switch to.
    :return: The string with lowercase.
    """
    if s:
        return s[0].lower() + s[1:]
    return s