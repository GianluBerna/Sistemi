def main():

    lista = [1, 'Ciao' , 3 , somma(3, 4)]

    for i in lista:
        print(i)

    print(lista)

    posizione = 1
    print(lista[-1])

    j = len(lista)
    print(j)



def somma(a, b):
    return a + b

main()

