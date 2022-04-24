def narcissistic(value):
    quantidade_numeros = len(str(value))
    exp = sum([(int(x) ** quantidade_numeros) for x in str(value)])
    if exp == value:
        return True
    else:
        return False

# Em uma única linha
def narcissistic_2(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))



print(narcissistic(153))