# Projeto criado para realizar as provas de Atila sobre bases númericas

from tkinter.constants import YES
from typing import List


def conversor_de_base_decimal(numero, base):
    return [x % base for x in gerador(numero, base)][::-1]  # Coleta os restos da divisão pelo valor da base, no fim, inverte os valores 

def gerador(valor, base):

    while valor >= 1:
        yield valor
        print(valor)
        
        valor = valor // base

print(conversor_de_base_decimal(465, 16))


def binario_para_x(valor, base=2):
    lista_valores = list(str(valor)[::-1])

    for conta in mostar_conta(lista_valores, base):
        print(conta)
    
    return sum([(int(p) * (base ** y)) for y, p in enumerate(lista_valores)])

def mostar_conta(lista_valores, base):
    for x, y in enumerate(lista_valores):
        yield f'{y} * {base} ^ {x} = {int(y) * base ** x}'


# print(f'O valor é {binario_para_x(1000001111, 2)} na base decimal')

