# def length_number(num):
#     contador = 0
#     for i in str(num):
#         contador += 1
#     return contador

# print(length_number(50000))
#-----------------------------
def length_number_2(num):   # Utilizando map
    a = sum(map(lambda x: 1, str(num))) 
    return a 

print(length_number_2(100))

# print(length_number(50000))
#---------------------------------------------
# Com ZIP

from itertools import count
a = zip(count(1), 'Thiago_SIlva')
a = list(a) #Transforma em lista para poder acessar o index
print(a[-1][0]) # Pega o index do ultimo elemento