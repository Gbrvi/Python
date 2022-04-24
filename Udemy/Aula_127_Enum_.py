from enum import Enum, auto

# #ENUM é como se fosse um dicionario, porém com algumas diferenças
# # Permite deixar mais organizado e mais limpo para quem estiver olhando o codigo
# # É para utilzar quando se tem um conjunto padrão de dados


# class Direcoes(Enum):
#     direita = auto()    # Defino minha variavel
#     esquerda = auto()   # Auto -> Da um valor aleatorio para variavel
#     cima = auto()
#     baixo = auto()

# class Game:
#     def movimentar(self, direcao):
#         if not isinstance(direcao, Direcoes):
#             raise ValueError('Cannot move to this direction')

#         return f'Moving {direcao.name}'


# a = Game()
# # print(a.movimentar('direita')) # Precisa chamar atributo da classe
# print(a.movimentar(Direcoes.direita))  
# print(a.movimentar(Direcoes.direita))  


# ----------------------------

# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3

# print(Color(2)) # Pode ser acessado o valor entre parenteses

#-----------------------------

class AutoName(Enum):   # Permite a mudança do auto()
     def _generate_next_value_(name, start, count, last_values):
         return name

class Ordinal(AutoName):
     NORTH = auto()
     SOUTH = auto()
     EAST = auto()
     WEST = auto()

# >> [<Ordinal.NORTH: 'NORTH'>, <Ordinal.SOUTH: 'SOUTH'>, <Ordinal.EAST: 'EAST'>, <Ordinal.WEST: 'WEST'>]


class Shape(Enum):
    SQUARE = 2
    DIAMOND = 1
    CIRCLE = 3
    ALIAS_FOR_SQUARE = 2

#>>> list(Shape)    # A variavel ALIAS, cujo tem o mesmo valor que Square, não será mostrada
# [<Shape.SQUARE: 2>, <Shape.DIAMOND: 1>, <Shape.CIRCLE: 3>]

for name, member in Shape.__members__.items():
    name, member    # Retorna todos as variaveis e não exclui os que possuem o mesmo valor

    # SQUARE Shape.SQUARE
    # DIAMOND Shape.DIAMOND
    # CIRCLE Shape.CIRCLE
    # ALIAS_FOR_SQUARE Shape.SQUARE

[name for name, member in Shape.__members__.items() if member.name != name] # Member nome é SQUARE, but name é Alias
   
    



