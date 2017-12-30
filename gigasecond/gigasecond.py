from datetime import date, timedelta

def add_gigasecond(date):
    """Calculate someone`s life in gigaseconds """
    return date + timedelta(0, 10 ** 9  )
