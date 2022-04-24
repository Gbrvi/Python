# The year can be evenly divided by 4, is a leap year,unless: 
    # The year can be evenly divided by 100, it is NOT a leap year, unless:
        # The year is also evenly divisible by 400. Then it is a leap year.


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def is_leap_2(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

print(is_leap_2(2000))