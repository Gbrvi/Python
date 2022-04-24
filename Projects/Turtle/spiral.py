import turtle

def desenho():
    a = turtle.Turtle()
    size_a = size_b = 1
    a.speed(0)
    a.color('cyan')
    a.pensize(2)
    for i in range(1000):
        a.forward(size_a)
        a.left(71)
        size_a += 1
        
turtle.bgcolor('black')
desenho()

turtle.mainloop()



