def solutions(a, b, c):
    bhaskara = (b**2) - (4*a*c)

    if bhaskara == 0:
        return 1
    elif bhaskara < 0:
        return 0

    return 2  




print(solutions(3, -15, 12))
print(solutions(1, 0, 0))
print(solutions(1, 0, 1))