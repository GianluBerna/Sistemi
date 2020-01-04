from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# 1)The error : 
#Traceback (most recent call last):
  #File "d:/Scuola/4AROB/Sistemi/Python/EsVacanze/Es02/Es02.py", line 3, in <module>
    #script, first, second, third = argv
#ValueError: not enough values to unpack (expected 4, got 1)

# 2)More arguments : 
#     script, first, second, third, fourth, fifth, sixth = argv
# Few arguments : 
#     script, first = argv

#3)
name = input("Nome: ")
print("Ciao " + name + " hai scritto ed esuguito uno script di nome " + script)