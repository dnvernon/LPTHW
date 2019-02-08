from sys import argv
#names the argument in the script
script, filename = argv
#gives the command to open the filename script
txt = open(filename)
#prints the contents of the file
print(f"Here's your file {filename}:")
print(txt.read())
#Prompts user to type the filename again
print("Type the filename again:")
file_again = input("> ")
#Prints the contents of the file again
txt_again = open(file_again)

print(txt_again.read())
