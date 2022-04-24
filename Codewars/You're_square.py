from math import trunc
def is_square(n):
    return n >=0 and trunc(n ** (1/2)) ** 2 == n

def is_square_2(n):
    return n >=0 and (n**(1/2)) % 1 == 0

    
print(is_square_2(10))