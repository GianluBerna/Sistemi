import socket as sck

def client():
    host = "127.0.0.1"
    porta = 4000

    client = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

    messaggio = input("inserire il messaggio : ")

    messaggio = bytes(messaggio , 'utf-8')

    client.sendto(messaggio ,(host , porta))

    data, address = client.recvfrom(4096)

    print(data)

    client.close()

if __name__ == '__main__':
    client()




