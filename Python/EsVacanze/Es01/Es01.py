types_of_people = 10        #assegno alla variabile il valore 10
x = f"There are {types_of_people} types of people."     #creo una variabile che contiene una stringa e che richiama una variabile intera

binary = "binary"   #variabile con una stringa
do_not = "don't"    #variabile con una stringa
y = f"Those who know {binary} and those who {do_not}."  #creo una variabile che contiene una stringa e che richiama due variabile con una stringa al loro interno

print(x)    #stampo la variabile x
print(y)    #stampo la variabile y 

print(f"I said: {x}")       #stampo una stringa che richiama la varibile x
print(f"I also said: '{y}'")    #stampo una stringa che richiama la varibile y

hilarious = False   #creo una variabile che che contiene False cioè un Bool

joke_evaluation = "Isn't that joke so funny?! {}"   #assegno alla variabile una stringa

print(joke_evaluation.format(hilarious))    #stampo una variabile e ci aggiungo il contenuto di un bool

w = "This is the left side of..."   #creo una variabile string
e = "a string with a right side."   #creo una variabile string

print(w + e)    #stampo le due variabili string concatenandole insieme