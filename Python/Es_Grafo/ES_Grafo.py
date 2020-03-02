def main():
    v = int(input("Inserire il numero di nodi : "))
    dict = creaDictDaNumNodi(v)
    stampaDict(dict)
    stampaMatrice(creaMatriceDaDict(dict, v), v)


def creaMatriceDaNumNodi(v):
    matrice = []
    for i in range(1, v + 1):
        e = [int(i) for i in input(f"Inserire le vicinanze del nodo {i} (separare con '/'): ").split('/')]
        colonna = [0 for dim in range(0, v)]
        for j in e:
            if j != i:
                colonna[j - 1] = 1
        matrice.append(colonna)

    return matrice


def creaDictDaNumNodi(v):
    dict = {}
    for r in range(0, v):
        chiave = r + 1
        occ = [int(i) for i in input(f"Inserire le vicinanze del nodo {chiave} (separare con '/'): ").split('/')]
        dict[chiave] = occ

    return dict


def creaDictDaMatrice(grafo):
    dict = {}
    for r in range(0, len(grafo)):
        chiave = r + 1
        occ = []
        for c in range(0, len(grafo)):
            if grafo[r][c] == 1:
                occ.append(c + 1)
        dict[chiave] = occ

    return dict


def creaMatriceDaDict(dict, v):
    matrice = []
    for key, val in dict.items():
        colonna = [0 for dim in range(0, v)]
        for link in val:
            colonna[link - 1] = 1
        matrice.append(colonna)

    return matrice


def stampaMatrice(matrice, v):
    for r in range(0, v):
        print(" ")
        for c in range(0, v):
            print(matrice[r][c], end=' ')
    return 0

def stampaDict(dict):
    for key, val in dict.items():
        print(f"{key}: {val},")

if __name__ == '__main__':
    main()