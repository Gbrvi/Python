class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y

    def __add__(self, other):
        soma_x = self.x + other.x
        soma_y = self.y + other.y
        return soma_x + soma_y
    
    def __radd__(self, other):
        return self.x + self.y + other  
    
    def __mul__(self, other):
        mult_x = self.x * other.x
        mult_y = self.y * other.y
        return mult_x * mult_y

    def __rmul__(self, other):
        return self.x * self.y * other
    
        
    

r1 = Retangulo(2, 3)
r2 = Retangulo(2, 5)
r3 = Retangulo(4, 1)
r4 = r1 * r2 * r3
print(r4)