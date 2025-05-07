import os.path
import socket
import tqdm


def receive_image():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostname(), 420))
    server.listen(5)

    connection, address = server.accept()
    print(f'connected to {address}')
    file_name = connection.recv(1024).decode('utf-8')
    file_size = connection.recv(1024).decode('utf-8')
    file_nonce = connection.recv(1024).decode('utf-8')
    file_tag = connection.recv(1024).decode('utf-8 ')
    receiver = connection.recv(1024).decode('utf-8')
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
    return file_nonce, file_tag, receiver, file_name


def send_image(image, ip, nonce, tag, receiver):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, 420))
    file = open(image, 'rb')
    file_size = os.path.getsize(image)
    client.send('sent.png'.encode('utf-8'))
    client.send(str(file_size).encode('utf-8'))
    client.send(nonce.encode('utf-8'))
    client.send(tag.encode('utf-8'))
    client.send(receiver.encode('utf-8'))
    data = file.read()
    client.sendall(data)
    client.send(b'<END>')
    file.close()
    client.close()
