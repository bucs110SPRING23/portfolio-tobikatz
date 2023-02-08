import pygame
pygame.init()

# gets the display and makes it full screen
# no arguments means full screen
screen = pygame.display.set_mode((250,300))

# RGB Scheme
# [R, G, B]=> [0-255, 0-255, 0-255]
screen.fill([255, 0, 0])
pygame.display.flip()

pygame.time.wait(500)

screen.fill([0, 255, 0])
pygame.display.flip()

pygame.time.wait(500)

screen.fill([0, 0, 255])

font = pygame.font.SysFont(None, 72)
text = font.render("Hello Tobi", True, "yellow")
# var = input()
screen.blit(text, screen.get_rect().center)

pygame.display.flip()

pygame.time.wait(2000)
# # waint until user quits
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

pygame.quit()
# 