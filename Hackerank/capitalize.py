def capitalize(nome):
    nome = nome.split(' ')
    return ' '.join((x.capitalize() for x in nome))


print(capitalize('1 w 2 r 3g'))