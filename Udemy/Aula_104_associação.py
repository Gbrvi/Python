# Associação é a mais fraca das três. Cada uma funciona por si só

class Escritor:
    def __init__(self, nome, ferramenta = None):
        self.__nome = nome
        self.__ferramenta = ferramenta
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta escrevendo...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina escrevendo...')

p1 = Escritor('Cauã')
caneta = Caneta('Big')
p1.ferramenta = caneta   # Envia tudo dentro de CANETA para a classe escritor
p1.ferramenta.escrever()