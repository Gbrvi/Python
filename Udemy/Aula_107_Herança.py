# Associação - Usa | Agregação - Tem | Composição - É | Herança - dono

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nomeclasse} falando...')

class Aluno(Pessoa):    #Herdou de pessoa todos seus metodos.
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')

class Client(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

p1 = Pessoa('Daniel', 62)
p1.falar()

a1 = Aluno('Thiago', 15)
a1.estudar()

c1 = Client('Ricardo', 40)
c1.comprar()
c1.falar()


