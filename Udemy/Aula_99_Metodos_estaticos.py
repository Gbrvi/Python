# Não precisa da instância nem classe.
# É uma função normal, mas por questão de organização está 
# dentro da classe
from random import randint

class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 99999)# Variavel apenas nesse metodo
        return rand

p1 = Pessoa('Luiz', 21)
p1.get_ano_nascimento()
print(Pessoa.gera_id())