import pygame
pygame.init()
screen = pygame.display.set_mode()
pygame.draw.circle(screen, "yellow", [100,100], 100)
pygame.display.flip()
pygame.draw.circle(screen,"red",[75,75],80)
pygame.display.flip()
pygame.draw.circle(screen,"green",[60,60],60)
pygame.display.flip()


