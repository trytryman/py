import turtle
import math
a=0
t1=turtle.Turtle()
t1.shape('turtle')

def w():
    turtle.setheading(90)
    turtle.forward(20)
def s():
    turtle.setheading(270)
    turtle.forward(20)
def a():
    turtle.setheading(180)
    turtle.forward(20)
def d():
    turtle.setheading(0)
    turtle.forward(20)
turtle.penup()
t1.penup()
turtle.pencolor('blue')
turtle.listen()
turtle.shape('turtle')
turtle.speed(3)
t1.pencolor('red')
t1.speed(1)
t1.setposition(70,70)
turtle.onkey(w,"w")
turtle.onkey(s,"s")
turtle.onkey(a,"a")
turtle.onkey(d,"d")


while True:

    rx=t1.xcor()
    ry=t1.ycor()
    tx=turtle.xcor()
    ty=turtle.ycor()
    a=math.atan2(ty-ry,tx-rx)
    a=math.degrees(a)
    t1.setheading(a)
    t1.forward(10)
    if(math.sqrt((tx-rx)*(tx-rx)+(ty-ry)*(ty-ry))<10):
        turtle.hideturtle()
        t1.hideturtle()
        break

turtle.done()
