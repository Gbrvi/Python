# Há 3 formas de representar uma string. !s -> string | !r -> representação de como o objeto se faz | !a -> ascii para conversar com qualquer coisa q nao saiba UTF8

from collections import namedtuple


print('{!r}'.format('Paçoca'))
# OUTPUT : 'Paçoca'

print('{!s}'.format('Paçoca'))
# OUTPUT : Paçoca

print('{!a}'.format('Paçoca'))
# OUPUT : 'Pa\xe7oca'

print('\n')

class MinhaString:
    def __init__(self, string='Paçoca'):
        self.string = string

    def __str__(self) -> str:   #!s
        return self.string

    def __repr__(self) -> str: # Retorna como o objeto é montado | !r
        return 'MinhaString(string=paçoca)'


print(f'{MinhaString()!r}') 
# OUTPUT : MinhaString(string=paçoca)

tuplazao = namedtuple('Pessoa', 'a b')

print(f'{tuplazao("Eduardo", "Ricardo") !s}')
# Pessoa(a='Eduardo', b='Ricardo')


# O uso do = | Mostra qual a variavel e não só o valor dela

nome = 'ração'

print(f'{nome=}')
# OUTPUT : nome='ração'

print(f'\n{nome.upper()=!a}')
# OUTPUT : nome.upper()='RA\xc7\xc3O'
