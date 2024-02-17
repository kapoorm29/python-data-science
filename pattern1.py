from turtle import *
speed(0)
def square():
    forward(100)
    right(90)

def hexagon():
    for i in range(6):
        forward(100)
        right(60)

def octagon():
    for i in range(8):
        forward(100)
        right(45)


for i in range(6):
    fd(100)
    octagon()
    hexagon()
    square()
    rt(60)
hideturtle()
mainloop()    