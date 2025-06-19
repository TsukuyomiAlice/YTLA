# coding=utf-8

def str_to_dict(in_put) -> dict:
    """Convert formatted string to dictionary using eval().

    Warning: Only use with trusted input sources as eval() can execute arbitrary code.

    Args:
        in_put (str): Input string in dictionary format (e.g. "{'key': 'value'}")

    Returns:
        dict: Parsed dictionary object
    """
    return eval(in_put)


def str_to_list(in_put) -> list:
    """Convert iterable string to list.

    Args:
        in_put (str): Input string (e.g. "abc")

    Returns:
        list: List of characters (e.g. ['a', 'b', 'c'])
    """
    return list(in_put)


def str_to_tuple(in_put) -> tuple:
    """Convert iterable string to tuple.

    Args:
        in_put (str): Input string (e.g. "123")

    Returns:
        tuple: Tuple of characters (e.g. ('1', '2', '3'))
    """
    return tuple(list(in_put))


def add_count_for_dict(key: str, dictionary: dict, count: int) -> dict:
    """Update count for specific key in dictionary.

    Args:
        key (str): Target key to update
        dictionary (dict): Dictionary to modify
        count (int): Value to add (can be negative)

    Returns:
        dict: Modified dictionary with updated counts
    """
    if key in dictionary.keys():
        dictionary.update({key: dictionary.get(key) + count})
    else:
        dictionary.update({key: count})
    return dictionary


def set_pick(check: list, base: list, exclude: list) -> list:
    """Filter elements present in check but not in base or exclude lists.

    Args:
        check (list): Source elements to filter
        base (list): Primary exclusion list
        exclude (list): Secondary exclusion list

    Returns:
        list: Elements from check that are not present in either base or exclude
    """
    res = []
    for element in check:
        if element not in base and element not in exclude:
            res.append(element)
    return res
