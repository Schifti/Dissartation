from PIL import Image
import binascii

'''
im = Image.open('pfp.png')
pix = im.load()
print(im.size)
width, height = im.size
print(width, 'x')
print(height, 'y')
print(pix[0, 0])
r, g, b, o = pix[0, 0]
print('R:', r, 'G:', g, 'B:', b, 'O:', o)
for x in range(0, width):
    for y in range(0, height):
        pix[x, y] = 255, 0, 255, 255
print(pix[0, 0])
im.save('test.png')
'''


def to_hex(msg):
    hexed = ''
    for char in msg:
        hexed = hexed + str(format(ord(char), 'x'))
    return hexed


def from_hex(hexmsg):
    return bytes.fromhex(hexmsg).decode('utf-8')


def encode(image, msg):
    im = Image.open(image)
    pix = im.load()
    width, height = im.size
    x, y = 0, 0
    c = 0
    for char in msg:
        if x >= height:
            y = y + 1
            x = 0
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
        x = x + 1
    im.save('test.png')
    return


def decode(image):
    im = Image.open(image)
    pix = im.load()
    width, height = im.size
    x, y = 0, 0
    c = 0
    msg = ''
    for x in range(0, width):
        for y in range(0, height):
            r, g, b, o = pix[x, y]
            if o == 254:
                if c == 0:
                    msg = msg + chr(r)
                    c = c + 1
                elif c == 1:
                    msg = msg + chr(g)
                    c = c + 1
                else:
                    msg = msg + chr(b)
                    c = 0
    return msg


encode('pfp.png', 'Martin Schifter')

print('Message:', decode('test.png'))
