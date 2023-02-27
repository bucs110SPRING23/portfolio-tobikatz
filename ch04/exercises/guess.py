
import random
x = random.randrange(0,1000)
amountoftries = []
guess =  1001
# for guesses in range(1000):
while guess != x:
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
        