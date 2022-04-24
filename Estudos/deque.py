'''Aprendendo Deque'''

from collections import deque

cache_values = deque(maxlen=4)  # Lista melhorada

# Pode ser inserido dos dois lados/ inserido em qualquer posição/ Pode rotacionar / E permite um tamanho máximo

def cache(func):
    def inner(*args):
        cache_values.append(args) # Adiciona valores, limite de 3
                        # Se adicionar mais valores, o primeiro será substituido
        return func(*args)
    return inner

@cache
def soma(x, y):
    return x + y

soma(2, 2)
soma(5, 5)
soma(8, 20)
soma(1, 70)

print(cache_values)
cache_values.rotate(1) # Positvo = Os ultimos vao pra frente, depender do valor
# / Negativo = Os primeiros vao para os ultimos/ depender do valor

print(cache_values)

