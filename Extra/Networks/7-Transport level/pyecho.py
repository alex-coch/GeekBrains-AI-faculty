import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2233))
s.listen(1)
while True:
    client, address = s.accept()
    while True:
        data = client.recv(1024)
        if not data: break
        if data == "Close" or data == "close": client.close()
        client.send(data)
client.close()

