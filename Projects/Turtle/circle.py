import turtle

def art():
    a = turtle.Turtle()
    a.speed(0)
    a.color('yellow')
    a.pensize(2)
    size = 1
    for i in range(250):
        a.circle(size)
        a.left(5)
        size += 2

turtle.bgcolor('black')
art()

turtle.mainloop()
