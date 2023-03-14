import pygame
# Part A
def threenp1(n):
    count = 0
    while n > 1.0:
       count += 1
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return count

def threenp1range(upper_limit):
    objs_in_sequence = { }
    for n,iters in range(2, upper_limit):
        threenp1(iters)
        objs_in_sequence[n] = iters
        return objs_in_sequence
       


def main():
   threenp1range(57)
   


main ()