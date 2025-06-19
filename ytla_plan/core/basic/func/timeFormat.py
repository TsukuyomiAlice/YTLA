# encode: utf-8
import datetime
import time


def get_current_time() -> str:
    """Get current time in standard format.

    Returns:
        str: Current time string in 'YYYY-MM-DD HH:MM:SS' format
    """
    time_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return time_string


def show_current_time() -> None:
    """Print current time to console in standard format.

    Outputs:
        Formatted time string prefixed with 'current time: '
    """
    time_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f'current time: {time_string}')


def get_today() -> str:
    """Get current date in standard format.

    Returns:
        str: Current date string in 'YYYY-MM-DD' format
    """
    date_string = time.strftime('%Y-%m-%d', time.localtime())
    return date_string


def calculate_date(date_string, time_delta) -> str:
    """Calculate date by adding/subtracting days.

    Args:
        date_string (str): Initial date in 'YYYY-MM-DD' format
        time_delta (int): Number of days to add (positive) or subtract (negative)

    Returns:
        str: New date string in 'YYYY-MM-DD' format
    """
    date_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    date_calculated = date_date + datetime.timedelta(days=time_delta)
    date_string = date_calculated.strftime("%Y-%m-%d")
    return date_string


def diff_date(date_str1, date_str2) -> int:
    """Calculate days difference between two dates.

    Args:
        date_str1 (str): First date in 'YYYY-MM-DD' format
        date_str2 (str): Second date in 'YYYY-MM-DD' format

    Returns:
        int: Number of days between date_str1 and date_str2 (date1 - date2)
    """
    date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d")
    d = (date1 - date2).days
    return d


def is_past_date(date_str) -> bool:
    """Check if a date is in the past or today.

    Args:
        date_str (str): Date to check in 'YYYY-MM-DD' format

    Returns:
        bool: True if date is today or in the past, False otherwise
    """
    if diff_date(time.strftime("%Y-%m-%d", time.localtime()), date_str) >= 0:
        return True
    else:
        return False


def datetime_abDHMSzY(datetime_str) -> datetime:
    """Parse datetime string with specific format.

    Args:
        datetime_str (str): Date string in 'Tue Mar 23 16:12:38 +0800 2021' format

    Returns:
        datetime: Parsed datetime object
    """
    time_format = datetime.datetime.strptime(datetime_str, '%a %b %d %H:%M:%S %z %Y')
    return time_format


def strtime_Ymd(datetime_time: datetime) -> str:
    """Format datetime object to compact date string.

    Args:
        datetime_time (datetime): Datetime object to format

    Returns:
        str: Date string in 'YYYYMMDD' format
    """
    time_string = datetime_time.strftime('%Y%m%d')
    return time_string
