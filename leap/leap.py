def is_leap_year(year):
    """ return True if the given year is leap and False if it`s not """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
