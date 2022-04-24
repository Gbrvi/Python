#Type é uma docstring. Não muda em nada o funcionamento do programa
#Serve apenas para informar

from typing import Union, List, NewType, TypeVar

Number = TypeVar('Number', int, float, complex)

def soma_numeros(x: Number, y: Number) -> Number:
    return x + y 


help(soma_numeros)