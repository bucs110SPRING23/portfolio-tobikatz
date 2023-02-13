import turtle
sides = (int(input("What is the number of sides")))
long = []
for _ in range(sides):
    length = (int(input("What is the length of each side")))
    long.append(length)
angle = 360/sides
pen = turtle.Turtle()
window = turtle.Screen()
pen.shape("turtle")
pen.color("blue")
for i in long:
    pen.forward(i)
    pen.left(angle)



window.exitonclick()
