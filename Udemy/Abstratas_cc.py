from Abstratas_conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite
    
    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self._saldo + self._limite) < valor:
            print('Saldo insuficiente')
            return

        self._saldo -= valor
        self.detalhes()

if __name__ == '__main__':
    a = ContaCorrente(2222, 3333, 10)
    a.sacar(10)
    a.sacar(1000)