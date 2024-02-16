"""Functions for working with dates."""

from datetime import datetime

SECONDS_IN_A_DAY = 86400


def convert_to_datetime(date: str) -> datetime:
    """Function that takes date string and return in datetime format"""
    try:
        date_x = datetime.strptime(date, '%d.%m.%Y')
        return date_x
    except:
        raise ValueError("Unable to convert value to datetime.")


def get_days_between(first: datetime, last: datetime) -> int:
    """Function that returns time difference between two dates"""

    try:
        time_d = last - first
        time_diff = int(time_d.total_seconds() // SECONDS_IN_A_DAY)
        return time_diff
    except:
        raise TypeError("Datetimes required.")


def get_day_of_week_on(date: datetime) -> str:
    """Function that returns readable day of the week"""
    try:
        return datetime.strftime(date, '%A')
    except:
        raise TypeError("Datetime required.")


print(get_day_of_week_on(datetime(1996, 10, 25)))
