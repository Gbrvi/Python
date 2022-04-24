# Praticando Classe

from random import randbytes, randint
class Pessoa():
    def __init__(self, nome):
        self.nome = nome
        self.id = randint(000000, 999999)
    
class Operario(Pessoa):
    def __init__(self, nome, work, capacete=None, ferramenta=None):
        super().__init__(nome)
        self.work = work
        self.capacete = capacete
        self.ferramenta = ferramenta
    
    def cor_capacete(self):
        if self.work == 'pedreiro':
            self.capacete = 'amarelo'
    
    def mostar_cor(self):
        return f'A cor do capacete é {self.capacete}'

class ferramentas():
    def __init__(self, item=None):
        self.item = item

    def usar(self):
        print(f'Utlizando {self.item}')


p1 = Operario('Rogério', 'pedreiro')
serra = ferramentas('serra')
p1.ferramenta = serra

p1.cor_capacete()
print(p1.mostar_cor())

p1.ferramenta.usar()
