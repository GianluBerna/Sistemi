def inipavimento(dim):
    pavimentoimento = []
    for r in range(0, dim):
        riga = []
        for c in range(0, dim): riga.append(True)
        pavimentoimento.append(riga)
    return pavimentoimento


def creapavimento():
    dim = int(input("Inserisci la dimensione del pavimentoimento: "))
    return inipavimento(dim)

def creaNodi(pavimento):
    nNodi = 1
    for r in range(0, len(pavimento)):
        for c in range(0, len(pavimento)):
            if pavimento[r][c]:
                pavimento[r][c] = nNodi
                nNodi += 1


def createDic(pavimento):
    dict = {}
    x = 1
    nNodi = 1
    for r in range(0, len(pavimento)):
        for c in range(0, len(pavimento)):
            links = []
            if pavimento[r][c] != False:                        #controlla se quella cella e vuota o no
                if r - x >= 0:                                  #controllo tutte le direzioni destra sinistra su giù
                    if (pavimento[r - x][c] != False):
                        links.append(pavimento[r - x][c])
                if c - x >= 0:
                    if (pavimento[r][c - x] != False):
                        links.append(pavimento[r][c - x])
                if c + x < len(pavimento):
                    if (pavimento[r][c + x] != False):
                        links.append(pavimento[r][c + x])
                if r + x < len(pavimento):
                    if (pavimento[r + x][c] != False):
                        links.append(pavimento[r + x][c])
                dict[nNodi] = links
                nNodi += 1
    return dict

def celleOccupate(pavimento):
    while True:                                                                                                           #chiede le celle occupate
        pos = input("Inserisci le cordinate della cella occupata (inserisci -1 per terminare) (prima riga e poi "         
                    f"colonna da 1 a {len(pavimento)}): ")
        if pos != "-1": pavimento[int(pos.split(".")[0]) - 1][int(pos.split(".")[1]) - 1] = False                         #le celle occupate inserisco false = (ostacolo)
        else:                                                                                                             #dove non c'è false c'è un numero
            if pos == "-1": break
    creaNodi(pavimento)
    return createDic(pavimento)


def main():
    p = creapavimento()
    for r in range(0, len(p)):
        print(" ")
        for c in range(0, len(p)): print(p[r][c], end=' ')
    print(" ")
    dict = celleOccupate(p)
    for r in range(0, len(p)):
        print(" ")
        for c in range(0, len(p)): print(p[r][c], end=' ')
    print(" ")
    for key, val in dict.items(): print(f"{key}: {val},")

if __name__ == '__main__':
    main()
