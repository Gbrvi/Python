class Calculator:
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b

calcultador = Calculator()
print(calcultador.add(10, 5))
print(calcultador.subtract(10, 5))
print(calcultador.multiply(10, 5))
print(calcultador.divide(10, 5))