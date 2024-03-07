from PIL import Image
import binascii

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


def to_hex(msg):
    hexed = ''
    for char in msg:
        hexed = hexed + str(format(ord(char), 'x'))
    return hexed


def from_hex(asciiHex):
    return bytes.fromhex(asciiHex).decode('utf-8')


def encode(image, msg):
    encoded = ''
    return encoded


def decode(encoded):
    msg = ""
    return msg


# Test
print(to_hex('hello world'))
print(from_hex('68656c6c6f20776f726c64'))
