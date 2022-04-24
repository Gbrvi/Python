# Exemplificando com pizza
class Pizza:
    pedacos = 5

    def __init__(self, sabor):
        self.sabor = sabor

    def pegar_pedaco(self):
        '''Metodo de instância'''
        self.pedacos -= 1   # Mesmo alterando na linha de baixo o tamanho da pizza, continua subtaindo o tamanho inciado padrão.
    
    @classmethod    # Precisa @classmethod para referenciar a classe
    def mudar_tamanho(cls, pedacos):
       cls.pedacos = pedacos    # Alterno o tamanho da Pizza

if __name__ == '__main__':
    
    cala = Pizza('Calabresa')

    cala.pegar_pedaco()
    cala.mudar_tamanho(12)
    cala.pegar_pedaco()

    print(cala.pedacos)
    print(Pizza.pedacos)