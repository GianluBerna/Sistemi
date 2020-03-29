import networkx as nx
import matplotlib.pyplot as plt


def caricaDati(nomeFile):
    data = open(nomeFile, 'r')      #apro il file in lettura
    lines = data.readlines()        #mi posiziono sulla sulla prima riga da leggere
    dict={}                         #creo un dizionario
    for line in lines:              #scorro tutta la lista
        lineSplit = line.split(' ')     #mi creo un array con i vari pezzettini della riga
        chiave = int(lineSplit.pop(0))  #nodo in cui ci troviamo
        nodi = [int(n) for n in lineSplit]  #nodi collegati
        dict[chiave]=nodi               #aggiungo tutto al dizionario
    data.close()
    return dict


def creaMatriceDaDict(dict):
    matrix = []
    for key, val in dict.items():
        colonna = [0 for dim in range(0, len(dict))]
        for link in val:
            colonna[link - 1] = 1
        matrix.append(colonna)

    return matrix


def stampaMatrice(matrix):
    for r in range(0, len(matrix)):
        print(" ")
        for c in range(0, len(matrix)):
            print(matrix[c][r], end=' ')


def stampaDict(dict):
    print("\n{")
    for key, val in dict.items():
        print(f"\t{key}: {val},")

    print("}")

def Elimina(lista):
     for i in lista:
         if lista.count(i) > 1:
             lista.remove(i)
             Elimina(lista)
     return lista


def trovaPazienteZero(dict):
    listaPazientiZero=[]
    for p in range(0, len(dict)): listaPazientiZero.append(trova(p, dict))      #cicla sul dizionario e assegna a listaPazientiZero per ogni cella un paziente Zero
    return Elimina(listaPazientiZero)           #passo tutta la lista e pulisco dei doppioni che vengono creati dal for


def trova(find, dict):
    tro = False
    for key, val in dict.items():           #for su tutto il dizionario
        if find in val:                     #controllo se il mio valore passato è presente nella lista val
            tro = True
            return trova(key, dict)         #richiamo la funzione e contiuno a cercare
    if tro == False: return find            #viene eseguito quando abbiamo scorso tutto il dizionario e non abbiamo trovato più la key impostata


def main():
    d = caricaDati("data.txt")
    #stampaDict(d)
    #m = creaMatriceDaDict(d)
    #stampaMatrice(m)
    lista = trovaPazienteZero(d)
    print(lista)



if __name__ == '__main__':
    main()