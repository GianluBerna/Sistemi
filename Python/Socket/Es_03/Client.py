import socket as sck

def client():
    host = "127.0.0.1"
    porta = 5000


    client = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

    client.connect((host , porta))

    messaggio = input("inserire il messaggio (per uscire scrivere exit) : ")

    while True:
        client.sendall(messaggio.encode())

        data = (client.recv(5096))
        data = data.decode()

        print(data)

        messaggio = input("inserire il messaggio (per uscire scrivere exit) : ")

        if messaggio == "exit":
            client.sendall(messaggio.encode())
            print("Connection close")
            break

    client.close()

if __name__ == '__main__':
    client()