# class Funcionarios:
#     def __init__(self, nome, sobrenome, idade):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.idade = idade

#     @property
#     def idade(self):
#         return self._idade
    
#     @idade.setter
#     def idade (self, valor):
#         if isinstance(valor, str):
#             valor = int(valor)

#         self._idade = valor

# p1 = Funcionarios('Thiago', 'Silva', '15')
# print(p1.nome)

class Gurizada:
    def __init__(self, primeiro, ultimo):
        self.primeiro = primeiro
        self.ultimo = ultimo
    
    @property
    def email(self):
        self._primeiro
        self._ultimo
        return '{}.{}@email.com'.format(self.primeiro, self.ultimo)

    @property
    def fullname(self):
        return f'{self.primeiro} {self.ultimo}'
    
    @fullname.setter
    def fullname(self, name):
        primeiro, ultimo = name.split(' ')
        self._primeiro = primeiro
        self._ultimo = ultimo

    

emp1 = Gurizada('John', 'Pereira')

emp1.fullname = 'Rogerio Ceni'

print(emp1.primeiro)
print(emp1.ultimo)
print(emp1.fullname)