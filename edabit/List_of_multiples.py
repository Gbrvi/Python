def list_of_multiples(num, length):
    multiplos = [num * x for x in range(1, length + 1)]
    return multiplos




print(list_of_multiples(12, 10))