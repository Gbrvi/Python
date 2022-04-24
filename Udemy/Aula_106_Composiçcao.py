# Composição um não funciona sem o outro. Endereco recebe a Classe dentro da Classe, diferente da agregação que recebe fora.
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

cliente = Cliente('Cauã', 20)
print(cliente.nome)
print(cliente.idade)

cliente.insere_endereco('Araruama', 'RJ')
cliente.insere_endereco('Juiz de fora', 'MG')

cliente.lista_enderecos()