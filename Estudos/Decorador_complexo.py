""" Praticando uso de decoradores"""

def decorador(argumentos_decorador):
    print(argumentos_decorador)
    """
    Parametros do decorador
    """
    def decorador_real(func):
        print(func.__name__)
        """ 
        Recebe a função 
        """
        def executar_funcao(x, y):
        #-------------- Só executa após ser instanciada-----------
            return func(x, y)
            """
            Executar a função
            """
        return executar_funcao
    return decorador_real

@decorador('Nestor')
def soma(x, y):
    return x + y

a = soma(2, 2)
print(a)