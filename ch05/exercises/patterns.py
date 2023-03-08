# Part A
def star_pyramid(x):
    star ="*"
    for i in range(x):
        print(star * (i + 1))
        i =+ 1



rows = int(input("How many rows: "))
star_pyramid(rows)


# Part B
def rstar_pyramid(y):
    star ="*"
    for i in range(y):
        print(star * (y))
        y = y-1



rows = int(input("How many rows: "))
rstar_pyramid(rows)
