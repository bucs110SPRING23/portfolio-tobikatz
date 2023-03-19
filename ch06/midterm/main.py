import turtle
import math 

def screen_dimensions():
    '''
   general function description: this function creates a screen
   args: (type) description
   return: (type) description
   '''
    window = turtle.Screen()
    window.bgcolor('gold')

def shapes ():
    '''
   general function description: This function draws the shapes
   args: (type) description
   return: (type) description
   '''
    pen = turtle.Turtle()
    pen.color('black')
    pen.shape('circle')


def main():
    screen_dimensions()
    shapes()





main ()