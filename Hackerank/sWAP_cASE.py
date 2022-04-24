def swap_case(s):
    indice = list()
    for x in s:
        if x.islower():
            indice.append(x.upper())
        elif x.isupper():
            indice.append(x.lower())
        else:
            indice.append(x)

    return ''.join(indice)
    

#List comprehension

def swap_case2(s):
    return ''.join([i.lower() if i.isupper() else i.upper() for i in s])

# Map
def swap_case3(s):
    return ''.join(map(lambda x: x.upper() if x.islower() else x.lower(), s))

# print(swap_case2('Pythonist 222'))
print(swap_case3('Pythonist 222'))