# # vending machines
# print("Welcome to the vending machine")
# code = input("Please enter a code: ")
# money = int(input("Give me money: "))

# def myvendingmachine():
#     if code == "A":
#         if money >= 1:
#             print("You got a coke")
#         else:
#             print("You need more money")
#     else:
#         print("invalid code")

# myvendingmachine()

##determine maximum value
def findmax(x,y,z):
    max = x
    if y > max:
        max = y
    if z > max:
        max = z
    print(max)

print("Please enter 3 numbers: ")
a = int(input(": "))
b = int(input(": "))
c = int(input(": "))    

findmax(a,b,c)
    