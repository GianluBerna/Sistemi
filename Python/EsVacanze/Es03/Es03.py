# import a module
from sys import argv

# stores the values contained by argv
script, filename = argv

# open the file
txt = open(filename)

# print use f-string
print(f"Here's your file {filename}:")
# print the contents of the file
print(txt.read())

print("Type the filename again:")
# input a file name
file_again = input("> ")
# open the file
txt_again = open(file_again)

# print the contents of the file
print(txt_again.read())
txt_again.close()