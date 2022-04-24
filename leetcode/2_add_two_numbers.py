def add_two(a, b):
    string_a, string_b = '', ''
    for num in a[::-1]:
        string_a += str(num)
    
    for num in b[::-1]:
        string_b += str(num)

    return [int(x) for x in str(int(string_a) + int(string_b))[::-1]]


print(add_two([0], [0]))

