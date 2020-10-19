import turtle


window = turtle.Screen()
window.setup(800,600)

dog = turtle.RawTurtle(window)
dog.shape('turtle')

dog.forward(200)
dog.right(90)
dog.forward(100)
dog.right(90)
dog.forward(200)
dog.right(90)
dog.forward(100)
dog.right(90)


window.exitonclick()
