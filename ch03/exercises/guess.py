
import random
x = random.randrange(0,11)
for guesses in range(3):
    guess =  int(input("Whats the number?"))
    if guess < x:
        print("Too Low")
    elif guess > x:
        print("Too High")
    else:
        print("Correct!")
        exit()
        