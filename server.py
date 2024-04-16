import tqdm
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 420))
server.listen(5)

connection, address = server.accept()
print(f'connected to {address}')
file_name = connection.recv(1024).decode('utf-8')
print(file_name)
file_size = connection.recv(1024).decode('utf-8')
print(file_size)
file = open(file_name, 'wb')
file_bytes = b''
done = False
progress = tqdm.tqdm(unit='B', unit_scale=True, unit_divisor=1000, total=int(file_size))
while not done:
    data = connection.recv(1024)
    if file_bytes[-5:] == b'<END>':
        done = True
    else:
        file_bytes += data
    progress.update(1024)
file.write(file_bytes)
file.close()
connection.close()
print(f'connected closed to {address}')
server.close()
