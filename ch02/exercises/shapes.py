import pygame
pygame.init()
screen = pygame.display.set_mode()
screen.fill("pink")
pygame.draw.circle(screen, "white", [600,550], 100)
pygame.draw.circle(screen, "black", [600,550], 100,3)
pygame.display.flip()
pygame.draw.circle(screen,"white",[600,450],75)
pygame.draw.circle(screen,"black",[600,450],75,3)
pygame.display.flip()
pygame.draw.circle(screen,"white",[600,350],60)
pygame.draw.circle(screen,"black",[600,350],60,3)
pygame.display.flip()
pygame.time.wait(3000)