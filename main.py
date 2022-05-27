from socket import (socket, AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET)
#localhsot, port 1234
HOST, PORT = "127.0.0.1", 1234
running =  b"HTTP/1.1 200 OK\n\nHello World!"

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)

    while True:
        try:
            connection, address = sock.accept()
            req = connection.recv(1024).decode('utf-8')
            result = req.split("\r\n")

            print(f"[INFO] Metodo [INFO]: {result[0]}")
            print(f"[INFO] Host [INFO]: {result[1]}")
            print(f"[INFO] Usuario requisitante [INFO]: {result[8]}")
            print(f"[INFO] Cookie [INFO]: {result[16]}")

            connection.sendall(running)
            connection.close()

        except Exception as E:
            print(E)