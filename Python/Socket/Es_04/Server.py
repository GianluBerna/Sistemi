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
    if cm == "avanti":
        tr.forward(num)
    if cm == "indietro":
        tr.backward(num)
    if cm == "destra":
        tr.right(num)
    if cm == "sopra":
        tr.left(num)


if __name__ == '__main__':
    server()