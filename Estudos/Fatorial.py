# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# def fatorial(x):
#     for c in range(x - 1, 0, -1):
#         x *= c
#     return x


# print(fatorial(0))

def fibonacci(x):
    a = 0
    b = 1
    for i in range(1, x):
        c = a + b
        a = b
        b = c
    return c

print(fibonacci(9))