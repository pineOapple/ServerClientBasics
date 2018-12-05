import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = '127.0.0.1'
# Bind the socket to the port
server_address = ('localhost', 55000)
print(f'starting up on {sys.stderr} port {server_address}')
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print(sys.stderr, f'waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print(f'connection from{client_address}')

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print(sys.stderr, 'received "%s"' % data)
            if data:
                print(sys.stderr, 'sending data back to the client')
                connection.sendall(data)
            else:
                print(sys.stderr, 'no more data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()