import turtle


def triangulo(some_triangulo):
    for _ in range(3):
        some_triangulo.forward(300)
        some_triangulo.left(120)
    
def screen():
    turtle.screensize(500, 500)

def art():
    t1 = turtle.Turtle()
    t1.speed(0)
    t1.color('red')
    t1.pensize(3)
    for _ in range(36):
        triangulo(t1)
        t1.left(10)
    
    t2 = turtle.Turtle()
    t2.color('yellow')
    t2.pensize(2)
    t2.speed(0)

    x = 1
    for i in range(460):
        t2.forward(x)
        t2.left(117)
        x  += 1
        if i == 300:
            t2.color('blue')

turtle.bgcolor('black')
art()
turtle.mainloop()

