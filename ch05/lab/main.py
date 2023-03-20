import pygame
# Part A
def threenp1(n):
    count = 0
    while n > 1.0:
       count = count + 1
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    while n == 1.0:
       return count

def threenp1range(upper_limit):
    threenplus1_dictionary = { }
    for n in range(2, upper_limit+1):
        iters = threenp1(n)
        threenplus1_dictionary[n] = iters
    return threenplus1_dictionary

def graph (value):
    points = threenp1range(value)
    coords = points.items()
    print(coords)
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    pygame.draw.lines(screen, "orange", False, list(coords))
    pygame.display.flip()
    new_screen = pygame.transform.flip(screen, False,True)
    width, height = new_screen.get_size()
    new_screen = pygame.transform.scale(new_screen,(width*5, height*5))
    new_screen.blit(new_screen,(0,0))
    pygame.display.flip()
    pygame.time.wait(1000)

    current_max = 0
    for key,value in coords:
        if value > current_max:
            current_max = value
        else:
           current_max != value
    print(current_max)
    font = pygame.font.Font(None,100)
    text = font.render(str(current_max), True, "green")
    pos = (10,10)
    screen.blit(text,pos)
    pygame.display.flip()
    pygame.time.wait(1000)

    return coords


def main():
   value = 600
   print (threenp1(value))
   print (threenp1range(value))
   graph(value)

main ()