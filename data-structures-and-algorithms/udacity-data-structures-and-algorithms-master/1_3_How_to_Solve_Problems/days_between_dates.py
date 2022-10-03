def is_leapyear(year: int) -> bool:
    """
    Checks if the given year is leap year or not.

    Args:
        year (int): year to be checked.
    
    Returns:
        Ture if the year is leap year, False otherwise.

    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(month: int, is_leapyear: bool=False) -> int:
    """
    Returns the number of days in a given month.

    Args:
        month (int): month of the year.
        is_leapyear (bool): whether the year is leap year or not.
    
    Returns:
        int: number of days in the given month.
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 28 if not is_leapyear else 29
    elif month in [4, 6, 9, 11]:
        return 30


def is_valid_input(year_from, month_from, day_from, year_to, month_to, day_to):
    """
    Returns True if the first date is before or same as the second date.
    """
    if year_from < year_to:
        return True
    if year_from == year_to:
        if month_from < month_to:
            return True
        if month_from == month_to:
            return day_from < day_to
    return False 


def daysBetweenDates(year_from, month_from, day_from, year_to, month_to, day_to):
    """
    Returns the age from a given date to another date. It is assumed that
    the later date is always bigger than the previous.

    Args:
        year_from (int): Start year.
        month_from (int): Start month.
        day_from (int): Start day.
        year_to (int): End year.
        month_to (int): End month.
        day_to (int): End day.
    
    Returns:
        int: Age between the given dates.
    """
    assert is_valid_input(year_from, month_from, day_from, year_to, month_to, day_to)

    days = 0
    if year_from == year_to:
        if month_from == month_to:
            days += day_to - day_from
            return days
        else:
            days += days_in_month(month_from, is_leapyear(year_from)) - day_from
            month_from += 1
            while month_from < month_to:
                days += days_in_month(month_from, is_leapyear(year_from))
                month_from += 1
            days += day_to
            return days
    else:
        days += days_in_month(month_from, is_leapyear(year_from)) - day_from
        month_from += 1
        while month_from < 13:
            days += days_in_month(month_from, is_leapyear(year_from))
            month_from += 1
        year_from += 1
        while year_from < year_to:
            days += 366 if is_leapyear(year_from) else 365
            year_from += 1
        month = 1
        while month < month_to:
            days += days_in_month(month, is_leapyear(year_from))
            month += 1
        days += day_to
        return days


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

if __name__ == '__main__':
    test()
