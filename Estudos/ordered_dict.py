from collections import OrderedDict

 # É dicionario q é ordenado na ordem que é colocado
 
dicionario = OrderedDict() 

# Adicionandos valores ao Dict

dicionario[0] = 20
dicionario[99] = '10'
dicionario[1] = 2
dicionario.update({35: 666, 11: 12, 00: 3, 000: 17})
# Print | OrderedDict([(0, 17), (99, '10'), (1, 2), (35, 666), (11, 12)])

# Há outro jeito de criar utilizando 'Key=Value'

meu_segundo_dict = OrderedDict(Maria=15, Ricardo=8, Python='Monstro')
# Print | OrderedDict([('Maria', 15), ('Ricardo', 8), ('Python', 'Monstro')])

# Ao alterar o valor de uma chave já existente, é substituido o valor, não altera o dicionario

meu_segundo_dict['Maria'] = 25 
# print | OrderedDict([('Maria', 25), ('Ricardo', 8), ('Python', 'Monstro')])

#Caso eu delete uma chave e reescreva ele, voltará para o final do dicionario! 

del meu_segundo_dict['Maria']
# print | OrderedDict([('Ricardo', 8), ('Python', 'Monstro')])
meu_segundo_dict['Maria'] = 0
# print | OrderedDict([('Ricardo', 8), ('Python', 'Monstro'), ('Maria', 0)])

# Posso definir um valor para todas as chaves de uma lista/tupla

menu_cardapio = ['Frango', 'Salada', 'Bife']

print(OrderedDict.fromkeys(menu_cardapio, 5))
# OrderedDict([('Frango', 5), ('Salada', 5), ('Bife', 5)])
