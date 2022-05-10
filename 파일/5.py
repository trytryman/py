import turtle
import math

def w():
    turtle.setheading(90)
    turtle.forward(10)
def s():
    turtle.setheading(270)
    turtle.forward(10)
def a():
    turtle.forward(180)
    turtle.forward(10)
def d():
    turtle.forward(0)
    turtle.forward(10)
turtle.setup(width = 2000, height = 2000)
turtle.shape('turtle')
turtle.speed(0)
wn=turtle.Screen()
wn.onkey(w,"w")
wn.onkey(s,"s")
wn.onkey(a,"a")
wn.onkey(d,"d")
wn.listen()