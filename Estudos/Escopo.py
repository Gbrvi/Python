'''Praticando escopo'''

var = 7 # Variavel global

def func():
    global var
    print(var)  #Primeiro procura no escopo local. Depois no global.
    var = 5
    print(var)


func()
print(var)