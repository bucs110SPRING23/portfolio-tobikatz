import pygame
import random
pygame.init()
screen = pygame.display.set_mode()
colors = ["red", "green", "blue", "yellow"]
random.shuffle(colors)
for color in colors:
	screen.fill(color)
	pygame.display.flip()
	pygame.time.wait(1000)
	screen.fill("black") #so you can tell what color it is in case its too fast
	pygame.display.flip()
	pygame.time.wait(250)
message = """
	simon says:
	UP: RED
	DOWN: BLUE
	LEFT: GREEN
	RIGHT : YELLOW
	Click on the window, enter sequence, then press enter 
"""

response = input(message)

#ISSUE: there are many events that occur, every movement of the mouse generates an event… we need a #way to filter through all the unnecessary events 

#pygame.EVENT_OBJECT

user_sequence = [] # to make sure they are hitting the correct buttons 
for event in pygame.event.get():
# we need to decide what the event type is
    if event.type == pygame.KEYDOWN:
    	if event.key == pygame.K_UP:
			screen.fill("red")
			user_sequence.append("red")
		if event.key == pygame.K_D:
            screen.fill("blue")
			user_sequence.append("blue")
        if event.key == pygame.K_LEFT:
            screen.fill("green")
			user_sequence.append("green")
        if event.key == pygame.K_RIGHT:
            screen.fill("yellow")
			user_sequence.append("yellow")



			
if user_sequence == colors:
	print("You win!!")
else:
	print("Were you paying attention?")

pygame.quit()
	
	
