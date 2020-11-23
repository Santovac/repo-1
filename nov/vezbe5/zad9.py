import turtle
window = turtle.Screen()
window.setup(800,600)
dog = turtle.RawTurtle(window)
dog.shape('turtle')
dog.color('red')

def move_up():
    global dog
    dog.goto(dog.xcor()+0, dog.ycor()+10)

def move_down():
    global dog
    dog.goto(dog.xcor()+0, dog.ycor()-10)

def move_right():
    global dog
    dog.goto(dog.xcor()+10, dog.ycor()+0)

def move_left():
    global dog
    dog.goto(dog.xcor()-10, dog.ycor()+0)

def pen_up():
    global dog
    dog.penup()

def pen_down():
    global dog
    dog.pendown()

turtle.listen()
turtle.onkeypress(move_up, 'w')
turtle.onkeypress(move_down, 's')
turtle.onkeypress(move_right, 'd')
turtle.onkeypress(move_left, 'a')
turtle.onkeypress(pen_up, 'z')
turtle.onkeypress(pen_down, 'x')

#turtle.mainloop()


window.exitonclick()