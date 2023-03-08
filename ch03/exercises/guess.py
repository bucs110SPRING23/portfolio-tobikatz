
import random
x = random.randrange(1,11) #random.randint(1,10) this is both inclusive
for _ in range(3):
    guess =  int(input("Whats the number?"))
    if guess < x:
        print("Too Low")
    elif guess > x:
        print("Too High")
    else:
        print("Correct!")
        break #we could have also put an if statement before these series (we would have needed to set guess to something random beforeahnd) of ifs that said if guess != num: 
        