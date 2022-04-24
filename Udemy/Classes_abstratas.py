# Classe abstrata não é iniciada 
# Metodos concetros -> Metodos normais
# Metodo abstrato -> Não tem corpo
from Abstratas_cc import ContaCorrente
from Abstratas_cp import ContaPoupanca


from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod # Com isso, será abstrada e não poderá ser instanciada
    def falar(self):
        pass

class B(A): # É obrigada a ter o método que foi abstrado 
    def cantar(self):
        pass

    def falar(self):
        pass

b = B()
# a = A() #Não pode instanciar classe abstrata 

cp = ContaPoupanca(1111, 2222, 20)
cp.depositar(10)
cp.sacar(10)
cp.sacar(10)
cp.sacar(10)
cp.sacar(10)



print('-------------------------------------')

cc = ContaCorrente(agencia=111, conta=333, saldo=0, limite=300)
cc.depositar(100)
cc.sacar(250)
cc.sacar(150)
cc.sacar(1)
