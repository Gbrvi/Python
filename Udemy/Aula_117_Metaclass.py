class Meta(type):
    def __new__(mcs, name, bases, namespace):
        #mcs -> Metaclasse
        #name -> Nome da classe
        #base -> Classes pai da das subsclasses
        #namespace -> Tudo que tem na classe em forma de dicionario 
        print(name)
        if name == 'A': # 
            return type.__new__(mcs, name, bases, namespace)
    
        if 'b_fala' not in namespace:
            print(f'ERRO! Você precisa criar b_fala em {name}') # Obriga a classe filha ter 'b_fala'
            
        else:
            if not callable(namespace['b_fala']):
                print('Precisa ser um método,não atributo! ')
        print(namespace)
        return type.__new__(mcs, name, bases, namespace) # Tem que retornar sempre, caso não tenha sido chamado anteriormente


class A(metaclass=Meta):    # Vai se comportar da maneira que a Classe META determinar.
    def falar(self):
        self.b_fala()

class B(A):
    def b_fala(self):   # Se esse metodo não existir, dará erro na classe A. 
        # É possivel utilizar classes abstratas, mas será utilizado metaclass
        ...
    def cantar(self):
        print('cantando...')
    
    thiago = 1


# b = B()
# b.b_fala()