TypeA = type('A', (), {'attr': 'Boa noite'})    # Nome da classe | Herda de alguém | o que vai ter na classe.

def bom_dia(self):
    print('bom dia')

def somando(self, x, y):
    return x + y

class Normal:
    x = 5

TypeB = type('TypeB', (), {'x' : 10, 'bom_dia': bom_dia, 'somando': somando})

t = TypeB()
t.bom_dia()
print(t.somando(2, 3))

normal = Normal()

