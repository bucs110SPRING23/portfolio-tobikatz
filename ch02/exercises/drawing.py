import turtle
sides = (int(input("What is the number of sides")))
for i in range(sides):
    length = (int(input("What is the length of each side")))
angle = 360/sides
pen = turtle.Turtle()
window = turtle.Screen()
pen.shape("turtle")
pen.color("green")

for sides in range(sides):
    pen.forward(length)
    pen.left(angle)
window.exitonclick()
