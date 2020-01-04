from sys import argv

# stores the values contained by argv
script, filename = argv

# print 3 string
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# input not memorized
input("?")

# other print
print("Opening the file...")

# open file
target = open(filename, 'w')

# simple print of a string
print("Truncating the file. Goodbye!")

# this line empties the file
target.truncate()

# print for ask 3 lines
print("Now I'm going to ask you for three lines.")

# 3 input for the lines
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# print which says it is starting to write to the file
print("I'm going to write these to the file.")

# write on the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# punto 3
target.write(line1 + "\n" + line1 + "\n" + line3 + "\n")

# print for says that the file will be closed
print("And finally, we close it.")

# close the file
target.close()

# punto 2
target = open(filename)
print("The contents of the file is: \n" + target.read())