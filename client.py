import socket

host = '192.168.1.205'
port = 420

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))

socket.send('Bingus'.encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))