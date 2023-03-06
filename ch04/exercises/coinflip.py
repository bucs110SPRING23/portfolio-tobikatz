import turtle
import random 

window = turtle.Screen()
player1 = turtle.Turtle()
player1.shape("turtle")
player1.color("green")
size = turtle.screensize()

while player1.pos() < size: #why is this not working!!!!
    movement = random.randint(1,100)
    if movement <= 50:
        player1.left(90)
        player1.forward(100)
        player1.pos()
    elif movement >=51:
        player1.right(90)
        player1.forward(100)
        player1.pos()
    
