import socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 6789))
while True:
    msg = server.recvfrom(1024)
    if (msg[0].decode() == "stop"):
        break
    print("client : ", msg[0].decode())
    data = input("Enter the message :")
    server.sendto(data.encode(), msg[1])
