# # Part A
# def star_pyramid(x):
#     star ="*"
#     for i in range(x):
#         print(star * (i + 1))
#         i =+ 1



# rows = int(input("How many rows: "))
# star_pyramid(rows)


# # Part B
# def rstar_pyramid(y):
#     star ="*"
#     for i in range(y):
#         print(star * (y))
#         y = y-1
# rows = int(input("How many rows: "))
# rstar_pyramid(rows)

# his method:

def star_pyramid(rows):
    for i in range (1, rows+1):  #range with one argument goes up to but not including
        print("*" * i)
def rstar_pyramid(rows):
    for i in range (rows,0,-1):
        print("*"*i)

levels = int(input("Enter Row Number: "))
star_pyramid(levels)
levels = int(input("Enter Row Number: "))
rstar_pyramid(levels)
