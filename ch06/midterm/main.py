import turtle
import math 


def deathly_hallows (side_length = 120):
    '''
   general function description: This function creates a screen and draws three shapes to create the harry potter deathly hallows symbol (a triangle, circle, and line)
   args: this function takes the argument of side_length, which allows for adjustments of the size of the shapes. 
   return: this function returns the amount of sides of the original shape i.e. the triangle
   '''
    # this sets up the screen
    screen = turtle.Screen()
    turtle.screensize(500,500,"gold")
    pen = turtle.Turtle()
    pen.color('red')
    pen.shape('circle')

    # invisibility cloak
    triangle = 3
    angle = 360/triangle
    
    for i in range(triangle):
        pen.forward(side_length)
        pen.left(angle)
        pen.forward(side_length)

    # sorcerors stone

    wand = math.sqrt(3) * side_length
    radius = (wand/3)
    pen.circle(radius)

    # elder wand
    pen.left(90)
    pen.forward(wand)
    
    screen.exitonclick()
    return triangle 


def main():
   deathly_hallows(193)


main ()