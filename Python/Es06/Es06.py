import random


def push(stack, element):
    stack.append(element)
    return stack


def pop(stack):
    return stack, stack.pop()


class carta(object):
    def __init__(self, seme, numero):
        self.seme = seme
        self.numero = numero

    def stampa(self):
        print(f"la carta ha seme {self.seme} con numero {self.numero}.")


def main():
    c = carta("C", 5)
    c.stampa()

    mazzo = []
    semi = ["C", "P", "D", "F"]

    for i in range(1, 14):
        for s in semi:
            push(mazzo, carta(s, i))

    for i in mazzo:
        i.stampa()

    rand = random.randint(0 , 52)

    for i in mazzo:
        if k < rand:




if __name__ == 'main':
    main()