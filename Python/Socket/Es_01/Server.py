import socket as sck

def server():
    host = "127.0.0.1"
    porta = 4000

    server = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

    server.bind((host, porta))

    data, address = server.recvfrom(4096)

    print(data)

    server.sendto(data, address)

    server.close()


if __name__ == '__main__':
    server()