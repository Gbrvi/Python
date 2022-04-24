'''Aprendendo default_dict'''

from collections import defaultdict

d = defaultdict(lambda: 'Não registado')    # Valor padrão caso não tenha a chave pedida

d['ctss']
d['a']
d['p']
d['abel'] = 8

print(d)
