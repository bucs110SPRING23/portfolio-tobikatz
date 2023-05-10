def main ():
    file_pointer = open("ideas.txt", "a")
    idea = input("Enter an idea: ")
    ideas = []
    ideas.append(idea)
    for i in ideas:
        file_pointer.write(i + "\n")
    file_pointer.close()
main ()