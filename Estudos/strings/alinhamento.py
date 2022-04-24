# Alinhamento são dado por :> para esquerda | :< para direita ou :^ centralizar

mercado = ['banana', 'maçã', 'pera', 'abacate']
preco = [5, 2, 3, 10]

for compra, valor in zip(mercado, preco):
    print(f'{compra:^8} {valor:^5}')