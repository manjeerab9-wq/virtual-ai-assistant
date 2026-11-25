"""Date and time responses."""

from datetime import datetime


def get_current_time(now=None):
    """Return the current local time in a readable format."""
    now = now or datetime.now()
    return now.strftime("It's currently %-I:%M %p.")


def get_current_date(now=None):
    """Return the current local date in a readable format."""
    now = now or datetime.now()
    return now.strftime("Today's date is %A, %B %-d, %Y.")
