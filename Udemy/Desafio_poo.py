from termcolor import colored
from colorama import init
from abc import ABC, abstractmethod
import abc
init()

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo
        self._verificado = False
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def numero_conta(self):
        return self._numero_conta
    
    @property
    def saldo(self):
        return self._saldo

    def deposito(self, valor):
        if not isinstance(valor, int):
            print('Apenas valores inteiros! ')
            return

        self._saldo += valor
        self.detalhes()
    
    def detalhes(self):
        print(f'Agencia: {self.agencia}'
             f'Conta: {self.agencia}'
             f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar():
        ...
    
class Pessoa():
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade

class Client(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None
    
    def inserir_conta(self, conta):
        self.conta = conta

class Banco:
    conta_banco = 65

    def __init__(self, cliente):
        self._cliente = cliente
        self._conta = cliente.conta
        
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def conta(self):
        return self._conta
    
    def checar(self):
        if self._conta.agencia == self.conta_banco:
            self._conta._verificado = True
              
class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite=100):
        super().__init__(agencia, numero_conta, saldo)
        self._limite = limite
        
    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if not self._verificado:
            print ('CONTA NÃO VERIFICADA')
            return
        
        if not isinstance(valor, int):
            print('APENAS VALORES INTEIROS')
            return
            
        if (self._saldo + self._limite) < valor:
            print(colored('ERRO! Valor excede o limite.', 'yellow'))
            return

        self._saldo -= valor
        self.detalhes()
    
class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)
    
    def sacar(self, valor):
        if not self._verificado:
            print('CONTA NÃO VERIFICADA')
            return 
        
        if not isinstance(valor, int):
            print('Apenas valores inteiros! ')
            return
        if valor > self._saldo:
            print(colored('Valor de saque superior ao saldo na conta.', 'red'))
            return

        self._saldo -= valor

if __name__ == '__main__':
    cp = ContaPoupanca(65, 555, 200)

    cc = ContaCorrente(65, 2222, 100)

    b = Client('Abel', 30)
    cliente_cp = Client('Adamastor', 15, cp)
    banco = Banco(cliente_cp, cp)

