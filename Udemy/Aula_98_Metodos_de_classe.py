#Metodo se for para ser utilizado pelo molde = cls
#Metodo se for para ser utilizado pela instancia = self
class Pessoa:
    ano_atual = 2021    #Metodos de classe referencia a classe não a instancia.

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod    #Necessita chamar sempre @classmetoh
    def por_ano_nascimento(cls, nome, ano_nascimento):  # Retorna o valor para classe
        idade =cls.ano_atual - ano_nascimento

        return cls(nome, idade)

p1 = Pessoa.por_ano_nascimento('Igor', 2000)
print(p1.idade)
p2 = Pessoa.por_ano_nascimento('Lucas', 15)
print(p2.idade)
p2.get_ano_nascimento()