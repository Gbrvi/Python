#  on every year that is evenly divisible by 4
#   except every year that is evenly divisible by 100
#     unless the year is also evenly divisible by 400

import re


def leap(year):
    if year % 4 == 0 and year % 100 !=0:
        return True
    elif year % 400 == 0:
        return True
    return False
    
print(leap(2016))