class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Sempre que eu pedir o valor PRECO esse metódo será chamado antes AQUI
    #Getter
    @property # Também tornar um metodo uma variavel.
    def preco(self):    # Chama o mesmo nome da variavel que vai alterar
        return self._preco
    
    #Setter 
    # Sempre que eu tentar atribuir um valor no 'preco' PRIMEIRO PASSARÁ AQUI.
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


p1 = Produto('Camisa', 100)
p1.desconto(10)
p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p1.preco)
print(p2.preco)