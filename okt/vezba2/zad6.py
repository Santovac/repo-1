import turtle
import math

a = float(input("Unesite a:"))
b = float(input("Unesite b:"))
c= math.sqrt(a*a+b*b)


window = turtle.Screen()
window.setup(800,600)

dog = turtle.RawTurtle(window)
dog.shape('turtle')
x,y= turtle.position()
dog.forward(a)
dog.right(90)
dog.forward(b)
dog.right(135)
dog.goto(x,y)


window.exitonclick()
