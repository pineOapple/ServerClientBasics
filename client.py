import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 55000
BUFFER_SIZE = 50
MESSAGE = "Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(b'hello?')
data = s.recv(BUFFER_SIZE)
s.close()

print(f"received data:{data}")
