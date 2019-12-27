import random


def main():

    nameList = ["Badoino Matteo","Bernardi Gianluca","Best Francesco" ,"Nardi Simone"]

    print(f"Interrogato: {nameList[random.randint(0,len(nameList)-1)]}")


if __name__ == '__main__':
    main()