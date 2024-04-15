import os.path
import socket

host = '10.59.8.145'
port = 420

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))
file = open('test.png', 'rb')
file_size = os.path.getsize('test.png')
socket.send('image.png'.encode('utf-8'))
socket.send(str(file_size).encode('utf-8'))
data = file.read()
socket.sendall(data)
socket.send(b'<END>')

file.close()
socket.close()
