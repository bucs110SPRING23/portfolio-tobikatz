import pygame
<<<<<<< HEAD
pygame.init()
screen = pygame.display.set_mode()
x = pygame.display.get_window_size() [0]/2
y = pygame.display.get_window_size() [1]/2
screen.fill("aquamarine1")
pygame.draw.circle(screen, "gold1",[x,y], 600)
=======
import random 
import math
pygame.init()
screen = pygame.display.set_mode((1000,1000))
screensize = pygame.display.get_window_size()
x = screensize [0]/2
y = screensize[1]/2
screen.fill("aquamarine1")
pygame.draw.circle(screen, "gold1",[x,y], y)
pygame.display.flip()
pygame.draw.line(screen,"hotpink2", (x+y, y), (x-y,y), width = 5 )
pygame.display.flip()
pygame.draw.line(screen,"hotpink2", (x, x + y), (x,y-x), width = 5 )
pygame.display.flip()


for _ in range(11):
    dartx = random.randrange(screensize [0])
    darty = random.randrange(screensize [1])
    distance_from_center = math.hypot(x-dartx,y-darty)
    is_in_circle = distance_from_center <= x
   
    if is_in_circle:
        dart = pygame.draw.circle(screen, "springgreen4", [dartx,darty], 15)
        pygame.display.flip()
        pygame.time.wait(1000)
    else:
         dart = pygame.draw.circle(screen, "red", [dartx,darty], 15)
         pygame.display.flip()
         pygame.time.wait(1000)


pygame.time.wait(5000)
>>>>>>> 3ed3fe3bca15db791bae9166ba6f3b6fd2892bc9
