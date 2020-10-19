import turtle


a = 100


window = turtle.Screen()
window.setup(800,600)

dog = turtle.RawTurtle(window)
dog.shape('turtle')

for i in range(3):
    dog.forward(a)
    dog.right(120)


window.exitonclick()
