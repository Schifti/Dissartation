import os
import socket

HOST = '192.168.1.205'
PORT = 420

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

while True:
    connection, address = server.accept()
    print(f'connected to {address}')
    msg = connection.recv(1024).decode('utf-8')
    print(f'msg is {msg}')
    connection.send(f'msg received'.encode('utf-8'))
    connection.close()
    print(f'connected closed to {address}')
