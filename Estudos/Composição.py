# Treinando conceitos de POO - Composição
from termcolor import colored
from colorama import init
from random import randint, random
init()

class Pizzaria:
    def __init__(self):
        self._pizzaolo = Pizzaolo()        
        self._limpeza = Limpeza()
        self._entregador = Motoboy()
        self._pratos = 0
        self._tem_pizza = False

    def pedido(self, pizza):
        self._pizzaolo.preparar_pizza(pizza)
        self._pratos += 1
        self._tem_pizza = True
    
    def limpar(self):
        self._limpeza.encaminar_pia(self._pratos)
        self._pratos -= 1
    
    def entregar(self):
        if self._tem_pizza:
            self._entregador.entregar()
        else:
            print('Nenhuma pizza para entrega')
        self._tem_pizza = False

class Forno:
    def __init__(self):
        self.pizzas = []
        self.lenha = None
    
    def assar(self, pizza):
        if not self.lenha:
            print('Não há lenha')
        else:
            print(f'Assando a pizza de {pizza}')
    
    def colocar_lenha(self):    
        self.lenha = True

class Pizzaolo:
    def __init__(self):
        self._forno = Forno()

    def preparar_pizza(self, pizza):
        self._forno.colocar_lenha()
        self._forno.assar(pizza)

class Limpeza:
    def __init__(self):
        self._louca = Louca()

    def encaminar_pia(self, pratos):
        self._louca.lavar_pratos(pratos)
    
class Louca:
    @staticmethod
    def lavar_pratos(pratos):
        if pratos >= 1:
            print(colored(f'Restam {pratos} pratos para serem lavados', 'green'))
            print('Lavando...')
        else:
            print('Não há pratos para serem lavados')

class Motoboy:
    def __init__(self):
        self._tempo = randint(10, 60)
    
    def entregar(self):
        print(colored(f'A pizza saiu para ser entregue. O tempo será aproximadamente {self._tempo} minutos', 'red'))


p1 = Pizzaria()

p1.entregar()
p1.entregar()


        
            
