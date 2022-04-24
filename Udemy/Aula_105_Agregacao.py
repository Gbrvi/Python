class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)
    
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor

        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

carrinho = CarrinhoDeCompras()

p1 = Produto('Camisa', 63)
p2 = Produto('Caneca', 20)
p3 = Produto('Notebook', 3500)
p4 = Produto('Alcool em Gel', 4.50)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p4)

carrinho.lista_produto()
print(carrinho.soma_total())