
dim = input("Quanti parole vuoi inserire ? : ")
l1 = []
l2 = []
for i in range(int(dim)):
    num = input("inserisci nome : ")
    l1.append(num)
print(l1)

p = input("Inserire la lunghezza da ricercare : ")

for i in l1:
    if len(i) >= int(p):
        l2.append(i)

print(l2)


