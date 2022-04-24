class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def __add__(self, other):
        soma_x = self.x + other.x
        soma_y = self.y + self.y
        return Retangulo(soma_x, soma_y)

a = Retangulo(1, 2)
b = Retangulo(3, 4)

c = a + b
print(c.x)