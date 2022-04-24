# Mini Linguagem

# Preenchimento -> Muito util pra tabulação

string = 'melão'

# print(f'{string:20} branco')

#OUTPUT : melão                branco

mercado = ['banana', 'maçã', 'pera', 'abacate']
preco = [5, 2, 3, 10]

for compra, valor in zip(mercado, preco):
    print(f'{compra:10} {valor:5}')
# OUTPUT: 
# banana         5
# maçã           2
# pera           3
# abacate       10


# -----------------------------------------