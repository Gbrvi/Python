
def quadrado(func):
    def inner(x):
        return func(x) ** 2
    return inner

def cubo(func):
    def inner(y):
        return func(y) ** 3
    return inner

def dividir(func):
    def inner(z):
        return func(z) // func(z)
    return inner

@dividir
@cubo
@quadrado
def valor(numero):
    return numero

print(valor(20))

       