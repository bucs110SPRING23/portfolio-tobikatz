import turtle
window = turtle.Screen()
player1 = turtle.Turtle()
size = turtle.screensize()
x = size[0]/2
y = size[1]/2
player1.goto(x,y)
window.wait(5000)
