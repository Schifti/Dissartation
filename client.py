import os.path
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 420))
file = open('test.png', 'rb')
file_size = os.path.getsize('test.png')
client.send('image.png'.encode('utf-8'))
client.send(str(file_size).encode('utf-8'))
data = file.read()
client.sendall(data)
client.send(b'<END>')

file.close()
client.close()
