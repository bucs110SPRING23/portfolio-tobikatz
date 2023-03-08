import turtle
import random 

window = turtle.Screen()
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("turtle")
player1.color("green")
size = turtle.screensize()
print (size)
is_in_screen = True

while is_in_screen: #why is this not working!!!!
    movement = random.randint(0,1)
    if movement == 0 :
        player1.left(90)
        player1.forward(50)
    elif movement == 1:
        player1.right(90)
        player1.forward(50)
# what if we could store the following data somewhere else not in the loop, and when it is needed it is found!
    turtlex = player1.xcor()
    turtley = player1.ycor()

    xrange = window.window_width() / 2
    yrange = window.window_height() / 2

    if abs(turtlex) > xrange or abs(turtley) > yrange:
        is_in_screen = False


