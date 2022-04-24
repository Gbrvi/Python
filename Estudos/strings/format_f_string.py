# Há duas formas de ter f string. Utilzando f'' ou .format

dicio = {
    'nome' : 'Eduardo',
    'idade' : '20',
    'pais' : 'Brasil',
}

# Aqui eu passo para uma variavel chamado S
s = ('Oi {nome}, vi que tem {idade} anos e você mora no {pais}')

# E desempacoto os determinados valores das chaves utilizando format

print(s.format(**dicio))

# Output: Oi Eduardo, vi que tem 20 anos e você mora no Brasil

#F string tem algumas desvantagens no dicionario

cadastro = {
    'nome' : 'Eduardo',
    'idade' : '20',
    'cpf' : '15967948761',
    'n_mae' : 'Gil',
    'n_pai' : 'Abel',
    'cidade' : 'Rio de Janeiro',
}

# É trabalhos utilizar com F string, fica muito codigo. Com format fica mais simples
print(f'{cadastro["nome"]} {cadastro["idade"]} {cadastro["n_mae"]} ')

string = '{0} {1} {4} {2}'

print(string.format(*cadastro.values()))

