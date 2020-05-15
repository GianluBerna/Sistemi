import socket as sck
import turtle


def server():
    host = "127.0.0.1"
    porta = 4000

    server = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

    server.bind((host, porta))

    lT = []


    while True:

        data, address = server.recvfrom(4096)
        data = data.decode()
        if address not in lT:
            lT.append(address)
            lT.append(turtle.Turtle())

        if address in lT:
            command(data, lT[lT.index(address)+1])

        if not data or data == "exit":
            print("Connection close")
            break

        server.sendto("Prossimo".encode(), address)


    server.close()

def command(move , tr):

    cm = move.split(",")[0]
    num = int(move.split(",")[1])
    switcher = {
        "avanti": avanti,
        "indietro": indietro,
        "destra": destra,
        "sinistra": sinistra,
    }
    switcher[cm](tr , num)

def avanti(tr, num):
    tr.forward(num)

def indietro(tr, num):
    tr.backward(num)

def destra(tr, num):
    tr.right(num)

def sinistra(tr, num):
    tr.left(num)

if __name__ == '__main__':
    server()