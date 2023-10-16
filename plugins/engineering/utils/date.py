from datetime import datetime, timedelta
from pendulum import timezone

TIME_ZONE = "America/Sao_Paulo"

def days_ago(n: int) -> datetime:
    """Return a date based on current time with -N days.

    Examples:
    >>> from engineering.utils.date import days_ago
    >>> print(days_ago(10))
    "2023-10-06 19:44:42.995874-03:00"

    Args:
        n (int): Number of days to reduce from the current date

    Returns:
        datetime: Return a current -N days in timezone `America/Sao_Paulo`
    """
    date_now = datetime.now(tz=timezone(TIME_ZONE)) - timedelta(days=n)

    return date_now


print(days_ago(n=10))
