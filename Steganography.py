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
        if pix[x, y] == pix[x + 1, y]:
            if c == 0:
                if r + ord(char) > 255:
                    pix[x, y] = r + ord(char)-256, g, b, o
                else:
                    pix[x, y] = r + ord(char), g, b, o
                c = c + 1
            elif c == 1:
                if g + ord(char) > 255:
                    pix[x, y] = r, g + ord(char)-256, b, o
                else:
                    pix[x, y] = r, g + ord(char), b, o
                c = c + 1
            else:
                if b + ord(char) > 255:
                    pix[x, y] = r, g, b + ord(char)-256, o
                else:
                    pix[x, y] = r, g, b + ord(char), o
                c = 0
    pix[random.randint(0, width - 1), random.randint(0, height - 1)] = 0, 255, 174, 255
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
        if pix[x, y] == (0, 255, 174, 255):
            return msg
        kr, kg, kb, ko = pix[x + 1, y]
        if c == 0:
            if r - kr < -1:
                msg = msg + chr(r - kr + 256)
            else:
                msg = msg + chr(r - kr)
            c = c + 1
        elif c == 1:
            if g - kg < -1:
                msg = msg + chr(g - kg + 256)
            else:
                msg = msg + chr(g - kg)
            c = c + 1
        else:
            if b - kb < -1:
                msg = msg + chr(b - kb + 256)
            else:
                msg = msg + chr(b - kb)
            c = 0


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


encode('pfp.png', "Hello World", 573909672895873)
print('Message:', decode('test.png', 573909672895873))
