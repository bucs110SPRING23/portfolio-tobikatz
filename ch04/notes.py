# #iteration = looping over some object
# # an object is iterable if it can be used in a loop

# mystr = "hello" #this IS iterable, even though every character in a word is a string, a special iterable list of characters
# mynums = [1,2,3,4,5] # this IS iterable, it can be looped over

# #anything that is iterable can be 'indexed' into, you can access some of it's internal data

# #we change anything in our list
# mynums[0] = 5
# print(mynums)

# # BUT a string cannot be assigned something new. 
# # Mutable (changeable) vs. Immutable (cannot be changed once it is created)
# #the integer 5 is an immutable object, strings are treated as immutable as well
# # == checks if two things are equal, but is checks if two things are the exact same object... 
# # bc things are mutable, two lists of equal value will never be the same. but strings are the same! this is bc they are immutable

# #substring using slice syntax
# mystr = "hello"
# print(mystr[0],mystr[1:4]) #print H go up to but don't include 4 "o"

# mystr = "J" + mystr[1:5] # this is a new string, you are not changing the old string, and that is why it is allowed
# print(mystr)

# print(mystr.lower(), mystr.upper(), mystr.capitalize())

# #iterable objects are not always mutable

# #slicing with mutable objects is super useful:
# mynums = [1,2,3,4,5]
# mynums [2:2] = [2.5,2.6] #2:2 makes it part of the list, and does not just stick in our list like [] within the other list
# print(mynums)  #if we spread out the 2:2 to like 2:4 it will overide the numbers in positions 2-4

# for i, v in enumerate(mynums): #this allows us to change things in mynums!!, there is no relationship between i and your index. 
#         # i == index location in the last, v == value at the index location
#         mynums[i] = v * 2
# print(mynums)

# for i in range(len(mynums)):
#         mynums[i] = mynums[i] *2
# print(mynums)

# mynums = (5,8,1,4,5) #using parentheses makes a list immutable... it is called a tuple!
# #cannot be assigned to!
# #tuples make the code much much faster!! 

# temp = x
# x= y
# y = temp #this is our basic swap algorithm, bc of tuples we can write the following:
# (x,y) = (y,x) #we don't even need the parentheses!!

# num = [5] * 3 
# print(num) #this prints 5 three times 

# num = (5) * 3
# print(num) #the computer guesses when there are single item tuples, it will therefore be treated as a tuple UNLESS we have a comma in there

# contacts = [
# ["bill", "867-5309"], ["jane", "308-0962"]
# ]
# name = input("Enter a name: ")
# #worst case scenario we have to loop n times, where n is the number of items
# for contact in contacts:
#     if contact [0] == name:
#         print(contact[1])
#         break



#this is called a dictionary

contact = {
        "bill":"867-5309", "jane":"308-0962"
    }
print(contact["jane"])

#list[index] = value
#dictionary[key] = value
#key/value pairs
#keys must be UNIQUE and IMMUTABLE (they are generally just strings)

contact["joe"] = "987-0987"
print(contact)
#we cant add two of the same key, it will just update the existing key!
for c in contact:
    print(c) #this prints out the key 
    print(contact[c]) #prints the value also 
for key, value in contact.items(): #this is enumerate for a dictionary!
    print(key) 
    print(value) 

for key in contact.keys(): #this is enumerate for a dictionary!
    print(key) 
    
#we can use get() for reading something

print(contact.get("juan")) #if it is not there it will say that its not there, allows us to safely check the dictionary

#data structures: stings, lists, tuples, and dictionaries