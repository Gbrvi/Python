# AGORA EU ENTENDI 
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def info(self):
        print(f'Nome: {self.nome} : idade {self.idade}')
    
class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
class Banco:
    def __init__(self):
        self.lista_agencia = [65, 20, 10]
        self.lista_conta = []
        self.lista_clientes = []
    
    def inserir_cliente(self, cliente):
        self.lista_clientes.append(cliente)
    
        # for x in self.lista_clientes:
        #     x.info()
    
    def informacao(self):
        for y in self.lista_clientes:
            print(y)

        
cliente_1 = Cliente('Marcelo', 40)
cliente_2 = Cliente('Mariazinha', 10)


conta_1 = Conta(10, 1111, 20)

banco = Banco()
banco.inserir_cliente(cliente_1)
banco.informacao()


