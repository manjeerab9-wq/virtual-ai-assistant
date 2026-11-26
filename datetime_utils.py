"""Date and time responses."""

from datetime import datetime

def get_current_time(now=None):
    """Return the current local time in a readable format."""
    now = now or datetime.now()
    hour = now.strftime("%I").lstrip("0")
    return f"It's currently {hour}:{now.strftime('%M %p')}."

def get_current_date(now=None):
    """Return the current local date in a readable format."""
    now = now or datetime.now()
    return f"Today's date is {now:%A}, {now:%B} {now.day}, {now:%Y}."
