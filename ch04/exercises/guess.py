
import random
x = random.randrange(0,1000)
amountoftries = []

for guesses in range(1000):
    guess =  int(input("Whats the number?"))
    amountoftries.append(guess)
    if guess < x:
        print("Too Low")
    elif guess > x:
        print("Too High")
    else:
        print("Correct!")
        break

print("It took ", len(amountoftries), " tries!")
        