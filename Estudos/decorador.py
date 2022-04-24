'''Praticando uso de decoradores'''

def decorador(func):  # Após ser decorada, func recebe a função soma
    print('Thiago')
    def inner(x, y):    # Inner recebe os parametros da função soma
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            return func(x, y)   # Realiza a operação de soma
        else:
            raise ValueError('Insira apenas inteiros')
    return inner

@decorador  # Quando eu chama soma, vai executar a função decorador
def soma(x, y):     # Decorando a função
    return x + y

print(soma(2, 8.2))