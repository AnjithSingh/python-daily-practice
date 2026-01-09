# Counting the number of days in a given month of a year

def no_of_days(month: int) -> int:
    """Return number of days in a given month (non-leap year)."""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 28
    else:
        return 30


def leap(year: int) -> bool:
    """Return True if year is a leap year, else False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Main program
year = int(input("Enter the year: "))
month = int(input("Enter the month number (1-12): "))

if month == 2 and leap(year):
    print("No of days:", 29)
else:
    print("No of days:", no_of_days(month))
