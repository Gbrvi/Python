from termcolor import colored
import turtle
import random

WIDTH, HEIGHT = 500, 500

CORES = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def quantidade_corredores():
    # while True:
    #     try:
    #         corredores = int(input('Escolha a quantidade de corredores (2-10): '))
    #         if 2 <= corredores <= 10:
    #             return corredores
    #         else:
    #             print(colored('Apenas apenas valores númericos entre (2-10)', 'red'))

    #     except ValueError:
    #         print('Apenas valores númericos')
    return 10

def init():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Corrida maluca')

def corrida(colores):
    linha_chegada()
    turtle = criar_corredores(cores)
    while True:
        for corredor in turtle:
            distancia = random.randrange(1, 20)
            corredor.forward(distancia)
            x, y = corredor.pos()
            if x >= WIDTH // 2 - 20:
                return cores[turtle.index(corredor)]

def criar_corredores(cores):
    turtles = []
    spacex = WIDTH// (len(cores) + 1)
    print(spacex)
    for i, color in enumerate(cores):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.speed(0)
        racer.penup()
        racer.setpos(-HEIGHT//2 + 10, -WIDTH//2 + ((i + 1) * spacex) )
        racer.pendown()
        turtles.append(racer)

    return turtles
    

def linha_chegada():
    chegada = turtle.Turtle()
    chegada.penup()
    chegada.forward(230)
    chegada.pendown()
    chegada.left(90)
    chegada.forward(230)
    chegada.backward(460)

corredores = quantidade_corredores()
init()

random.shuffle(CORES)
cores = CORES[:corredores]

print(corrida(cores))
turtle.mainloop()
