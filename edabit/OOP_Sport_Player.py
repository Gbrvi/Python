class Player:
    def __init__(self, name, age, height, weight):
        self._name = name
        self._height = height
        self._weight = weight
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        self._height = height

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, weihgt):
        self._weight = weihgt

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

    def get_age(self):
        return f'{self._name} is age {self._age}'
    
    def get_height(self):
        return f'{self._name} is {self._height} cm'

    def get_weight(self):
        return f'{self._name} weighs {self._weight}'

p1 = Player('Gabriel', 19, 160, 62)

p1.age = 15
p1.weight = 80
p1.height = 180
p1.name = 'Lucas'
print(p1.get_age())
print(p1.get_height())
print(p1.get_weight())
print(p1.weight)
print(p1.height)
print(p1.age)
print(p1.name)

