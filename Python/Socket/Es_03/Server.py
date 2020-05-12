import socket as sck

def server():
    host = "127.0.0.1"
    porta = 5000

    server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

    server.bind((host, porta))

    server.listen()
    conn, address = server.accept()

    while True:

        data = (conn.recv(5096))
        data = data.decode()
        print(address, ":", data)

        if not data or data == "exit":
            print("Connection close")
            break

        conn.sendall(data.encode())

    conn.close()

if __name__ == '__main__':
    server()