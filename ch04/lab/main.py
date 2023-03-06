import pygame
import random 
import math

pygame.init()
screen = pygame.display.set_mode()
x = pygame.display.get_window_size() [0]/2
y = pygame.display.get_window_size() [1]/2
screen.fill("aquamarine1")
pygame.draw.circle(screen, "gold1",[x,y], 750)

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
playergreen = []
playerpink = []

results= ()

done = False
hitboxes = {
    "pink" : pygame.Rect(0,0,50,50),
    "green" : pygame.Rect(0,0,50,50)
}

hitboxes["pink"].topleft = hitboxes["green"].topright

colors = {
    "pink" : (255,105,180),
    "green" : (34,139,34)
}

while not done:
    for c,hb in hitboxes.items():
            pygame.draw.rect(screen,colors[c],hb)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hitboxes["pink"].collidepoint(event.pos):
                results = "pink"
            elif hitboxes["green"].collidepoint(event.pos):
                results = "green" 
    for _ in range(11):
                for i in range(2):
                    dartx = random.randrange(screensize [0])
                    darty = random.randrange(screensize [1])
                    distance_from_center = math.hypot(x-dartx,y-darty)
                    is_in_circle = distance_from_center <= x
                    if i == 0:
                        if is_in_circle: 
                            dart = pygame.draw.circle(screen, "springgreen4", [dartx,darty], 15)
                            pygame.display.flip()
                            pygame.time.wait(500)
                            playergreen.append("hit")
                        elif not is_in_circle: 
                            dart = pygame.draw.circle(screen, "green", [dartx,darty], 15)
                            pygame.display.flip()
                            pygame.time.wait(500)
                            
                    elif i == 1 :
                        if is_in_circle: 
                            dart = pygame.draw.circle(screen, "pink", [dartx,darty], 15)
                            pygame.display.flip()
                            pygame.time.wait(500)
                            playerpink.append("hit")
                        elif not is_in_circle:
                            dart = pygame.draw.circle(screen, "pink4", [dartx,darty], 15)
                            pygame.display.flip()
                            pygame.time.wait(500)
           
            
                            

    print(playerpink)
    print(playergreen)

    if len(playergreen) > len(playerpink):
        if results == "green":
            font = pygame.font.Font(None, 48)
            text = font.render("Green player won, correct!", True, "black")
            screen.blit(text, (x,y))
            pygame.display.flip()
        else:
            font = pygame.font.Font(None, 48)
            text = font.render("Green player won, incorrect!", True, "black")
            screen.blit(text, (x,y))
            pygame.display.flip()

    elif len(playergreen) < len(playerpink):
        if results == "pink":
            font = pygame.font.Font(None, 48)
            text = font.render("Pink player won, correct!", True, "black")
            screen.blit(text, (x,y))
            pygame.display.flip()
        else:
            font = pygame.font.Font(None, 48)
            text = font.render("Pink player won, incorrect!", True, "black")
            screen.blit(text, (x,y))
            pygame.display.flip()

    else:
        if results == "pink" or "green":
            font = pygame.font.Font(None, 48)
            text = font.render("Tie Game!", True, "black")
            screen.blit(text, (x,y))
            pygame.display.flip()

    
    done = True

pygame.time.wait(1000)
