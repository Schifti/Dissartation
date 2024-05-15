from Steganography import encode, decode
from AES import key_gen
from p2p import send_image, receive_image


def steganography():
    end = False
    while not end:
        choice = input('Would you like to: \n(E)ncode \n(D)ecode \n(B)ack \n')
        if choice.lower() == 'e':
            image = input('Input image name\n')
            message = input('What message\n')
            key = input('Input key\n')
            nonce, tag = encode(image, message, key)
            print('Message Encoded')
            print('Nonce:', nonce, 'tag', tag)
        elif choice.lower() == 'd':
            image = input('Input image name\n')
            nonce = input('Input nonce\n')
            tag = input('Input tag\n')
            key = input('Input key\n')
            print('Message:', decode(image, nonce, tag, key))
        elif choice.lower() == 'b':
            return
        else:
            print('Error please try again')
    return


def communication():
    end = False
    while not end:
        choice = input('Would you like to: \n(S)end \n(R)eceive \n(B)ack \n')
        if choice.lower() == 's':
            image = input('Input image name\n')
            ip = input('Input IP address\n')
            nonce = input('Input nonce\n')
            tag = input('Input tag\n')
            receiver = input('Input recipients username\n')
            send_image(image, ip, nonce, tag, receiver)
        elif choice.lower() == 'r':
            receive_image()
        elif choice.lower() == 'b':
            return
        else:
            print('Error please try again')
    return


def main():
    end = False
    while not end:
        choice = input('Would you like to: \n1). Encode or Decode messages \n2). Send or Receive messages \n3). '
                       'generate a key\n4). Quit \n')
        if choice == '1':
            steganography()
        elif choice == '2':
            communication()
        elif choice == '3':
            print('key:', key_gen())
        elif choice == '4':
            return
        else:
            print('Error please try again')
    return


main()
