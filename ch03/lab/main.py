import pygame
pygame.init()
screen = pygame.display.set_mode()
x = pygame.display.get_window_size() [0]/2
y = pygame.display.get_window_size() [1]/2
screen.fill("aquamarine1")
pygame.draw.circle(screen, "gold1",[x,y], 600)
