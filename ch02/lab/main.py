# part A
# Race 2
import turtle
import random 
screen = turtle.Screen()
player1 = turtle.Turtle()
player1.color("pink")
player1.shape("turtle")
player2 = turtle.Turtle()
player2.color("orange")
player2.shape("turtle")
player1.up()
player2.up()
player1.goto(-100,20)
player2.goto(-100,-20)
player1.down()
player2.down()
x = random.randrange(1,101)
y = random.randrange(1,101)
for _ in range (1):
    player1.forward(x)
    player2.forward(y)
    player1.up()
    player2.up()
    player1.goto(-100,20)
    player2.goto(-100,-20)
    player1.down()
    player2.down()
    player1.clear()
    player2.clear()

# Race 1
player1.forward(20)
player2.forward(90)
player1.goto(-100,20)
player2.goto(-100,-20)
player1.down()
player2.down()

screen.exitonclick()

