import random 
import pygame

class LED:
    """ docstring for Point"""
    def __init__(self,x=0, y=0, color="red"): # what the self is doing is representing the instance being created
        # self.xcoor = abs(x) # allows us to ensure it is positive!
        # self.ycoor = abs(y)
        self.on = True
        self.rect = pygame.Rect(abs(x), abs(y), 5,5)
        self.color = color
        self.radius = 10
    #there is no return statment 

    #we can add another function

    def random_color(self):
        """ sets point to a new random color"""
        new_color = [
                    "red", "green", "blue", "yellow"
                     ]
        self.color = random.choice(new_color)