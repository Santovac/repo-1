import turtle


a = float(input("Unesite a:"))
b = float(input("Unesite b:"))

window = turtle.Screen()
window.setup(800,600)

dog = turtle.RawTurtle(window)
dog.shape('turtle')

dog.forward(a)
dog.right(90)
dog.forward(b)
dog.right(90)
dog.forward(a)
dog.right(90)
dog.forward(b)
dog.right(90)

window.exitonclick()
