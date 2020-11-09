import turtle

def create_window(name,w,h):
    w = int(w)
    h = int(h)
    window = turtle.Screen()
    window.title(name)
    window.setup(w,h)
    return window

def create_turtle(x, y,shp,clr):
    dog = turtle.RawTurtle(window)
    #dog.setposition(-100,-100)
    dog.shape(shp)
    dog.color(clr)
    dog.goto(x, y)
    return dog

window = turtle.Screen()
window.setup(800,600)
width = [-400, -400, 400, 400]
height = [-300, 300, -300, 300]
shp='turtle'
clr='red'

#x = int(input('Input x coordinate: '))
#y = int(input('Input y coordinate: '))
for i in range(4):
    create_turtle(width[i], height[i],shp,clr)
name = input('Window name: ')
w = input('Window width: ')
h = input('Window height: ')
create_window(name,w,h)
window.exitonclick()