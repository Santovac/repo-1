import turtle


window = turtle.Screen()
window.setup(800,600)

dog = turtle.RawTurtle(window)
dog.shape('turtle')
for i in range(4):
    dog.forward(50)
    dog.right(90)

window.exitonclick()
