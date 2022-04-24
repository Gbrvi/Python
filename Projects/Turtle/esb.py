import turtle

def art():
    a = turtle.Turtle()
    a.speed(0)
    a.color('blue')
    a.pensize(2)
    size = 1
    for i in range(250):
        a.left(20)
        a.forward(i)
        a.left(90 + size)
        a.forward(i)
        size += 1
        
turtle.bgcolor('black')
art()

turtle.mainloop()