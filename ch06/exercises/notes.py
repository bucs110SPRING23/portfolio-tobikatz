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

import json

data = {
    "num" : 1,
    "msg" : "Hello World",
}

json_string = json.dumps(data)
print(json_string, type(json_string))

json_data = json.loads(json_string)
for k,v in json_data.items():
    print(k,v)

fptr = open("assets/data.json", "w")
fptr.write(json_data)
fptr.close()