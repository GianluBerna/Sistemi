import threading
import logging
from random import randint

biglietti = 100
s1 = threading.Lock()

def cassa():
    global biglietti
    s1.acquire()

    rnd = randint(1, 10)
    logging.info(f"Sono il cliente {threading.get_ident()} e voglio acquistare {rnd} biglietti")

    if biglietti >= 0:
        if biglietti >= rnd:
            print("Biglietti aquistati : ", rnd)
            biglietti = biglietti - rnd
            print("Biglietti disponibili : ", biglietti)
        else:
            print("Biglietti aquistati : ", biglietti)
            biglietti = 0
            print("Biglietti disponibili : ", biglietti)

    s1.release()


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    t1  = [threading.Thread(target=cassa) for _ in range(0, 30)]

    for i in t1:
        i.start()

    for i in t1:
        i.join()

if __name__ == '__main__':
    main()