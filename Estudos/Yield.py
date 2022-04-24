def gen():
    yield 1
    yield 2

a = gen()
print(next(a))
# 1
print(next(a))
# 2

def gen_print():
    print('Inicio da geração')  
    print('antes do 1')
    yield 1
    print('Depois do 1')
    print('antes do dois')
    yield 2
    print('depois do dois')
    print('Final da função geradora')
print('----------------------------------')
b = gen_print()
print(next(b))  #Inicio da geração/ antes do 1/ 1
print(next(b))  #Depois do 1/ antes do dois/ 2


print('----------------------------------')

def my_generator():
    yield from [1, 2, 3, 4, 5]

def sem_yield_from():
    for valor in [1, 2, 3, 4, 5]:
        yield valor

mg = my_generator()
print(next(mg)) # 1
print(next(mg)) # 2
print(next(mg)) # 3
print(next(mg)) # 4
print(next(mg)) # 5

print('---------------------------')
def capitulos():
    yield 1
    yield from sub_capitulos()
    yield 2

def sub_capitulos():
    yield 1.1
    yield 1.2
    yield 1.3

cap = capitulos()
print(next(cap)) # 1
print(next(cap)) # 1.1
print(next(cap)) # 1.2
print(next(cap)) # 1.3
print(next(cap)) # 2

print('-------------------------')
# --------------- EXPRESSÕES GERADORAS ------------------
g = (n for n in range(100) if n % 2 == 0)

