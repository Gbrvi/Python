from math import inf, trunc
def getMiddle(string):
    t = len(string) / 2 
    t = trunc(t)

    if len(string) % 2 == 0:
        return string[t - 1: t + 1]

    elif len(string) % 2 != 0:
        return string[t]

# Sem utilizar trunc
def get_middle2(string):
    t = int(len(string) / 2)
    if len(string) % 2 == 0:
        return string[t - 1: t + 1]
    else:
        return string[t]

#Utilizando divmod

def get_middle3(string):
    index, odd = divmod(len(string), 2)
    return string[index] if odd else string[index - 1: index + 1]


print(get_middle3('Test'))
print(get_middle3('meddlet'))