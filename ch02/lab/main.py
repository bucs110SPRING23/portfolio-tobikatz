# part A
# Race 2
import turtle
import random 
import pygame
import math
pygame.init()

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

# Part B
window = pygame.display.set_mode()
window.fill("pink")
listofshapes =[3,4,6,20,100,360]
points = []
side_length = 350
xpos = 600
ypos = 600
for i in range(6):
    num_sides = listofshapes[i]
    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = xpos + side_length *math.sin(radians)
        coordinate = (x,y)
        points.append(coordinate)

    pygame.draw.polygon(window,"blue",points)
    pygame.display.flip()

    pygame.time.delay(1500)

    window.fill("pink")
    points = []

