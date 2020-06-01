import socket

HOST = "127.0.0.1"
PORT = 5487

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = input("(Press q to exit)Welcome to 1A2B game!, make your guess:  ")
while True:
    if message == "q":
        break
    client.sendall(message.encode())
    serverMessage = str(client.recv(1024), encoding="utf-8")
    message = input(serverMessage)
client.close()
