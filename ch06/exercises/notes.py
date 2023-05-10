# # program that counts the amount of abc characters in the file

# def main():
#     filename = "assets/data.json"
#     fptr = open(filename, "r")
#     accumulator = 0
#     for ch in fptr.read():
#         if ch.isalnum (): #an alphanumerical character
#             accumulator += 1

#     fptr.close()

#     fptr = open(filename + ".dat", "w") #added a new extension so the previous one wasn't overwritten
#     data = str(accumulator) + "characters" # any variable you want to turn into a string you can also do f"{accumulator} charachters"
#     fptr.write(data) #write ONLY takes strings
#     fptr.close()

# main ()

# import json

# data = {
#     "num" : 1,
#     "msg" : "Hello World",
# }

# json_string = json.dumps(data)
# print(json_string, type(json_string))

# json_data = json.loads(json_string)
# for k,v in json_data.items():
#     print(k,v)

# fptr = open("assets/data.json", "w")
# fptr.write(json_data)
# fptr.close()

   
    
import point
import turtle
import random 
import pygame

# p1 = point.Point(3,4,"yellow") # p1 is an instance of point, and Point is a class
# p1.x = 52
# print(p1.x, p1.y, p1.color, type(p1), id(p1))
# #p1.x = 10 # allows us, to access the internal variable, it does not go out of scope until the object is out of scope. 

# #state of p1 has an x of 10, and p2 has an x of 5. 
# # y and color for both are unchanged

# points = []
# for p in range(10):
#     x = random.randint(0,100)
#     y = random.randint(0,100)
#     points.append(point.Point(x,y))

# t = turtle.Turtle()
# for p in points:
#     p.random_color()
#     t.color(p.color)
#     t.goto(p.x, p.y)

# turtle.Screen().exitonclick()

pygame.init()
display = pygame.display.set_mode()
p1 = point.LED(x=100, y = 100)

pygame.draw.circle(display, p1.color, (p1.rect.x, p1.rect.y), p1.radius )

while True: #this jsut keeps the screen open
    pygame.display.flip()
