import socket as sck

def server():
    host = "127.0.0.1"
    porta = 4000

    server = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

    server.bind((host, porta))

    while True:

        data, address = server.recvfrom(4096)
        data = data.decode()
        print(address, data, "=", eval(data))

        if not data or data == "exit":
            print("Connection close")
            break

        d = str(eval(data)).encode()
        server.sendto(d, address)

    server.close()


if __name__ == '__main__':
    server()