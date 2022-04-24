# Esse é mais complexo. Defino o valor de (i) atraves de range.
# O valor de X virá quando interar a função
def create_multiplications(n):
    return [(lambda i: lambda x : x * i) (i) for i in range(n)]

# Dois argumentos, declarando que i = i do for 
def create_multiplications_2(n):
    return [(lambda x, i=i : x * i) for i in range(n)]

for m in create_multiplications(4):
    print(m(4))