#Part A
import random

weeks = 16
print("weeks",type(weeks))
classes = 5
print ("classes", type(classes))
tuition = 6000
print ("tuition", type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print("cost_per_week", type(cost_per_week))
classes_per_week = [3,2,1,3,2]
print("classes_per_week", type(classes_per_week))
print("Cost per week:", cost_per_week)
print ("Cost for class A is:", cost_per_week / classes_per_week[0])
print ("Cost for class B is:", cost_per_week / classes_per_week[1])
print ("Cost for class C is:", cost_per_week / classes_per_week[2])
print ("Cost for class D is:", cost_per_week / classes_per_week[3])
print ("Cost for class E is:", cost_per_week / classes_per_week[4])


# part B
myList = ["Hufflepuff","Gryffindor","Slytherin","Ravenclaw",3.14159, 11]
hogwarts_house_or_math = random.choice(myList)
print(hogwarts_house_or_math)