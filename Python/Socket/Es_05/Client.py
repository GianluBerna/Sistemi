import socket as sck

def client():
    host = "127.0.0.1"
    porta = 4000

    client = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

    messaggio = input("inserire il comando(per uscire scrivere exit) : ")

    while True:

        client.sendto(messaggio.encode(), (host , porta))

        data = client.recv(4096)

        print("-", data.decode())

        messaggio = input("inserire il comando(per uscire scrivere exit) : ")


        if messaggio == "exit":
            client.sendto(bytes(messaggio, 'utf-8'), (host, porta))
            print("Connection close")
            break

    client.close()

if __name__ == '__main__':
    client()

