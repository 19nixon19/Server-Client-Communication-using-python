import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("127.0.0.1", 6789)
while True:
    msg = input("Enter the message: ")
    client.sendto(msg.encode(), addr)
    data = client.recvfrom(1024)
    if (data[0].decode() == "stop"):
        break
    print("Server :", data[0].decode())
