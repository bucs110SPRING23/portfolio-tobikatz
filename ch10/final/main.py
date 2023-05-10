import requests 
from cat import Cat
from randomfacts import Randomfacts


def animalquiz(cat,nope):
    """
    the user will be given a series of questions to determine if they like cats. 
    args: cat and nope
    return: their scores for cat and nope
    """
    start = input("type begin to start  ")
    if start == "begin":
        print("For each statement, write T for true and F for false")

        q1 = "I don't have a cat."
        q2 = "I am extroverted"
        q3 = "I love to be social"
        q4 = "I am spontaneous"
       

        questions = (q1, q2, q3, q4)

        for q in questions:
            print(q)
            answer = input("Your answer:  ").upper()
            if answer == "T":
                nope +=1
            elif answer == "F":
                cat +=1
            else:
                print("Please start again")
                exit()


        return (cat,nope)
    else:
        print("you don't want to play?")
def main():
    cat = 0
    nope = 0 
    catscore, nopescore = animalquiz(cat, nope)
    if catscore > nopescore:
        print("You're a cat person! Here is a cat fact :)")
        catFact = Cat(num =catscore)
        print(catFact.get())
        exit()
    else:
        print("Since you don't seem to like cats, here is some random advice!")
        advice = Randomfacts()
        print(advice.get())
        exit()



main()

