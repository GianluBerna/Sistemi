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



def stampaMatrice(matrice):
    for r in range(0, len(matrice)):
        print(" ")
        for c in range(0, len(matrice)):
            print(matrice[r][c], end=' ')
    return 0




def AlgoritmoDijkstra(mat):
    inizio = int(input("\nInserire il nodo da cui partire : "))
    succ = [x for x in range(0, len(mat))]
    dist = [100000 for _ in range(0, len(mat))]
    dist[inizio] = 0
    nodi = []
    pesi = []
    prec = []
    precedenti = inizio

    while len(succ) > 0:                #ciclo finche ci sono elementi successivi
        i = min(dist)
        z = dist.index(i)
        nodo = succ.pop()
        dist.remove(i)
        nodi.append(nodo)
        pesi.append(i)
        prec.append(precedenti)

        for nVicini in mat[nodo]:                                   #ciclo for sulla matrice con indice il nodo
            if nVicini > 0 and mat[nodo].index(nVicini) in succ:    #mi chiedo se ci sono ancora elementi
                y = mat[nodo].index(nVicini)
                nViciniSucc = succ.index(y)
                distanza = nVicini + i
                if distanza < dist[nViciniSucc]:                    #controllo se la distanza totale è minore di quella in quel nodo
                    dist[nViciniSucc] = distanza
                    mat[nodo][y] = 0
        precedenti = nodo

    return nodi, pesi, prec



def main():
    #v = int(input("Inserire il numero di nodi : "))
    mat = [[0, 1, 4, 0],
            [1, 0, 1, 3],
            [4, 1, 0, 1],
            [0, 3, 1, 0]]
    stampaMatrice(mat)
    nodi, pesi, prec = AlgoritmoDijkstra(mat)

    print(nodi)
    print(pesi)
    print(prec)


if __name__ == '__main__':
    main()