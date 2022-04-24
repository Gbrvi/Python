# Write a Python program to check if a specified element presents in a tuple of tuples.

cores = (('Red', ('White', 'Blue')), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

def verificador(tupla, cor):
    for x in range(len(tupla)):
        if cor in tupla[x]:
            return True
    return False

print(verificador(cores, 'White'))

def verificador_2(tupla, cor):
    return any(cor in x for x in tupla)

print(verificador_2(cores, 'White'))