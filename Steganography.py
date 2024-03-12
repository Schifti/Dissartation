from PIL import Image
import random


def encode(image, msg, seed):
    im = Image.open(image)
    pix = im.load()
    width, height = im.size
    c = 0
    random.seed(seed)
    for char in msg:
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        r, g, b, o = pix[x, y]
        if c == 0:
            pix[x, y] = ord(char), g, b, 254
            c = c + 1
        elif c == 1:
            pix[x, y] = r, ord(char), b, 254
            c = c + 1
        else:
            pix[x, y] = r, g, ord(char), 254
            c = 0
    x, y = random.randint(0, width - 1), random.randint(0, height - 1)
    pix[x, y] = 0, 255, 174, 254
    im.save('test.png')
    return


def decode(image, seed):
    im = Image.open(image)
    pix = im.load()
    width, height = im.size
    c = 0
    msg = ''
    random.seed(seed)
    end = False
    while not end:
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        r, g, b, o = pix[x, y]
        if o == 254:
            if pix[x, y] == (0, 255, 174, 254):
                return msg
            if c == 0:
                msg = msg + chr(r)
                c = c + 1
            elif c == 1:
                msg = msg + chr(g)
                c = c + 1
            else:
                msg = msg + chr(b)
                c = 0


def main():
    end = False
    while not end:
        choice = input('Would you like to: \n(E)ncode \n(D)ecode \n(Q)uit \n')
        if choice == 'E':
            encode('pfp.png', "Hello World I hate everyone!", 573909672895873)
            print('Message Encoded')
        elif choice == 'D':
            print('Message:', decode('test.png', 573909672895873))
        elif choice == 'Q':
            end = True
        else:
            print('Error please try again')
    return


main()
