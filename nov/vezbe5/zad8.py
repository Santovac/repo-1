import turtle
window = turtle.Screen()

def create_window(path):
    f = open(path, 'r')
    parameters = f.readlines()
    parameters = parameters[0].split(',')
    parameters[0] = int(parameters[0])
    parameters[1] = int(parameters[1])
    window.setup(parameters[0],parameters[1])
    window.title(parameters[2])
    f.close()


path = input('Path: ')
create_window(path)
window.exitonclick()