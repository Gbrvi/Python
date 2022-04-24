class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')

class Client(Pessoa):
    def falar(self):
        print('Tô em clientes')

class ClientVIP(Client):
    def falar(self):
        #super().falar() # Se refere a classe superior (Client)
        print('Outra coisa qualquer')

class ClientPremium(ClientVIP):
    def falar(self):
        Pessoa.falar(self) # Chama diretamente da class que deseja. É necessário identificar os parametos.
        # super().falar()
        ClientVIP.falar(self) 
        print('Oi')
    
class ClientUltra(ClientPremium):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome 
    
    def falar(self):
        ClientPremium.falar(self) #Chama falar de ClientePremium
        print(f'{self.nome} {self.sobrenome}')


c3 = ClientUltra('Jurubeba', 5, 'Pernambucana')
c3.falar()