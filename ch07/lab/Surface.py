import pygame 
import Rectangle

class Surface:
    """this class creates a rectangle and takes variables such as filename, x coordinate
    y coordinate, height and width of the rectangle. it returns the internal rectangle attribute
    """
    def __init__(self,filename, x,y,h,w):
        self.image = filename 
        self.rect = pygame.Rect(abs(x), abs(y), abs(w),abs(h)) 
    
    def getRect(self):
        return self.rect
        
