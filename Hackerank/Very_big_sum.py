# lista = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

# soma = 0
# for c in lista:
#     soma += c

# print(soma)

# Em função

def soma_grande(x):
    soma = 0
    for i in x:
        soma += i

    return soma

print(soma_grande([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))

# Em classe

class Soma:

    def __init__(self, valores):
        self.valores = valores
    

    def somando(self):
        soma = 0
        for i in self.valores:
            soma += i
        return soma

primeira_lista = Soma([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])

print(primeira_lista.somando())
            
        
        