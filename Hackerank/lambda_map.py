def fibonacci(n):
    a = 1
    b = 0
    fibo = []
    for _ in range(n):
        fibo.append(b)
        d = a + b
        a = b
        b = d
    return fibo

cube = lambda x: x ** 3

n = int(input('numero'))

print(list(map(cube, fibonacci(n))))


# Recursion 
# def fibonacci_2(n):
#     if n <= 1:
#         return n

#     return fibonacci_2(n - 1) + fibonacci_2(n - 2)

# print(fibonacci_2(10))
