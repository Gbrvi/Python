# def iniciador(nome):
#     def mensagem(msg):
#         return msg + ' ' + nome
#     return mensagem


# a = iniciador('Carlos')
# print(a('Bom dia'))
    

# Decorador

def decorando(func):
    def inner(nome, idade, genero):
        if genero == 'feminino':
            return f' Sra {nome} com {idade} anos '
        elif genero == 'masculino':
            return f' Sr {nome} com {idade} anos '
        else:
            return 'ERRO! Apenas sexo masculino ou feminino'
    return inner

@decorando
def pessoa(nome, idade, genero):
    return f'{nome} {idade}'


c = pessoa('Noc', 45, 'feminino')
print(c)


