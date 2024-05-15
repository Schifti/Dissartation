from Steganography import encode, decode
import secrets


def key_gen():
    key = secrets.token_hex(32)
    return key


def main():
    end = False
    while not end:
        choice = input('Would you like to: \n(e)ncode \n(d)ecode \n(q)uit \n')
        if choice == 'e':
            encode('pfp.png', "Hello World", 573909672895873)
            print('Message Encoded')
        elif choice == 'd':
            print('Message:', decode('test.png', 573909672895873))
        elif choice == 'q':
            end = True
        else:
            print('Error please try again')
    return
