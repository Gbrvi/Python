from turtle import Turtle, Screen, right, screensize
import turtle

def screen():
    turtle.screensize(500, 500)
    turtle.bgcolor('black')

def square(some_square):
    for _ in range(4):
        some_square.forward(200)
        some_square.right(90)

def square_2(some_square):
    for _ in range(4):
        some_square.left(90)
        some_square.forward(200)


def art():
    noc = turtle.Turtle()
    noc.color('blue')
    noc.pensize(2)
    noc.speed(0)
    for _ in range(40):
        square(noc)
        noc.left(1)

    piki = turtle.Turtle()
    piki.color('yellow')
    piki.pensize(2)
    piki.speed(0)
    for _ in range(40):
        square_2(piki)
        piki.left(1)

    abel = turtle.Turtle()
    abel.color('red')
    abel.pensize(2)
    abel.speed(0)


screen()
art()

turtle.exitonclick()



