from turtle import *

speed('fastest')
bgcolor('black')
pencolor('blue')
n=0
while n <= 200:
    fd(100 + n)
    rt(360/6)
    write(n, font=('calibri',15))
    n += 5

hideturtle()
mainloop()