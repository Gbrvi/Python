'''Treinando dicionarios'''

dicionario = {'dictA': {'nome': 'Gabriel', 'idade': 20},
        'dictB': {'nome': 'Abel', 'idade': 30},
}
dicionario['dictC'] = {'nome': 'Nestor', 'idade': '11'}


dictt = {'marca': 'acer', 'placa': 12345}


# Get evita levantar erros
'''print(dicionario.get('dictD'))'''  # None

dictt.update({'marca_2' : 'hp', 'dono': 'Alline'})

print(dictt)