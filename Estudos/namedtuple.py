from collections import namedtuple
# É tipo um dicionario, é mais lento, mas é imutável!

            #Jogador é a classe  |   #Atributos da classe
J = namedtuple('Jogador', ['nome', 'time', 'camisa', 'numero'])


j = J('Abel Hernadez', 'Flu', 99, 100)  #Adicionando valores
j2 = J('Fred', 'Fluminense', 9, 157)    

print(j2.nome)

#-------------------------------------------------------

# Nomes repetidos ou destinado ao python (def, class) são subtituidos se colocar o rename
P = namedtuple('Pessoa', ['nome', 'idade', 'def'], rename=True)

p = P('Carlos', 15, 'viano')
#output: Pessoa(nome='Carlos', idade=15, _2='viano')


#Default define um valor padrão, mas é nececssario que o primeiro valor "x" seja informado
L = namedtuple('valores', ['x', 'y', 'z'], defaults=(None, None))

l = L(2)
print(l)