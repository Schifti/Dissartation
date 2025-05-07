from PIL import Image
import random
from AES import encrypt, decrypt


def to_hex(char):
    hexed = ''
    if char <= 9:
        hexed = hexed + str(char)
    elif char == 10:
        hexed = hexed + 'a'
    elif char == 11:
        hexed = hexed + 'b'
    elif char == 12:
        hexed = hexed + 'c'
    elif char == 13:
        hexed = hexed + 'd'
    elif char == 14:
        hexed = hexed + 'e'
    elif char == 15:
        hexed = hexed + 'f'
    return hexed


def encode(image, msg, key):
    im = Image.open(image)
    pix = im.load()
    width, height = im.size
    c = 0
    try:
        r, g, b = pix[0, 0]
        coords = []
        random.seed(key)
        nonce, ciphertext, tag = encrypt(msg, key)
        for char in ciphertext:
            x, y = random.randint(0, width - 2), random.randint(0, height - 2)
            r, g, b = pix[x, y]
            while pix[x, y] != pix[x + 1, y]:
                pix[x, y] = 100, 100, 100
                x, y = random.randint(0, width - 2), random.randint(0, height - 2)
            for loc in coords:
                if (x, y) == loc or (x + 1, y) == loc:
                    skip = True
            coords.append((x, y))
            coords.append((x + 1, y))
            r, g, b = pix[x, y]
            char = int(char, 16)
            if c == 0:
                if r + char > 255:
                    pix[x, y] = r + char - 256, g, b
                else:
                    pix[x, y] = r + char, g, b
                c = c + 1
            elif c == 1:
                if g + char > 255:
                    pix[x, y] = r, g + char - 256, b
                else:
                    pix[x, y] = r, g + char, b
                c = c + 1
            elif c == 2:
                if b + int(char) > 255:
                    pix[x, y] = r, g, b + char - 256
                else:
                    pix[x, y] = r, g, b + char
                c = 0
        pix[random.randint(0, width - 2), random.randint(0, height - 2)] = 0, 255, 174
        im.save('encoded.png')
        return nonce, tag

    except:
        coords = []
        random.seed(key)
        nonce, ciphertext, tag = encrypt(msg, key)
        for char in ciphertext:
            x, y = random.randint(0, width - 2), random.randint(0, height - 2)
            r, g, b, o = pix[x, y]
            while pix[x, y] != pix[x + 1, y]:
                pix[x, y] = r, g, b, 254
                x, y = random.randint(0, width - 2), random.randint(0, height - 2)
            for loc in coords:
                if (x, y) == loc or (x + 1, y) == loc:
                    skip = True
            coords.append((x, y))
            coords.append((x + 1, y))
            r, g, b, o = pix[x, y]
            char = int(char, 16)
            if c == 0:
                if r + char > 255:
                    pix[x, y] = r + char - 256, g, b, o
                else:
                    pix[x, y] = r + char, g, b, o
                c = c + 1
            elif c == 1:
                if g + char > 255:
                    pix[x, y] = r, g + char - 256, b, 0
                else:
                    pix[x, y] = r, g + char, b, 0
                c = c + 1
            elif c == 2:
                if b + int(char) > 255:
                    pix[x, y] = r, g, b + char - 256, 0
                else:
                    pix[x, y] = r, g, b + char, 0
                c = 0
        pix[random.randint(0, width - 2), random.randint(0, height - 2)] = 0, 255, 174, 255
        im.save('encoded.png')
        return nonce, tag


def decode(image, nonce, tag, key):
    im = Image.open(image)
    pix = im.load()
    width, height = im.size
    c = 0
    msg = ''
    try:
        r, g, b = pix[0, 0]
        random.seed(key)
        end = False
        while not end:
            x, y = random.randint(0, width - 2), random.randint(0, height - 2)
            r, g, b = pix[x, y]
            if pix[x, y] == (0, 255, 174):
                unhex = bytes.fromhex(msg)
                return decrypt(nonce, unhex, tag, key)
            kr, kg, kb = pix[x + 1, y]
            if pix[x, y] == (100, 100, 100):
                o = 255
            elif c == 0:
                if r - kr < 0:
                    msg = msg + to_hex(r - kr + 256)
                else:
                    msg = msg + to_hex(r - kr)
                c = c + 1
            elif c == 1:
                if g - kg < 0:
                    msg = msg + to_hex(g - kg + 256)
                else:
                    msg = msg + to_hex(g - kg)
                c = c + 1
            else:
                if b - kb < 0:
                    msg = msg + to_hex(b - kb + 256)
                else:
                    msg = msg + to_hex(b - kb)
                c = 0
        return
    except:
        random.seed(key)
        end = False
        while not end:
            x, y = random.randint(0, width - 2), random.randint(0, height - 2)
            r, g, b, o = pix[x, y]
            if pix[x, y] == (0, 255, 174, 255):
                unhex = bytes.fromhex(msg)
                return decrypt(nonce, unhex, tag, key)
            kr, kg, kb, ko = pix[x + 1, y]
            if o == 254:
                o = 255
            elif c == 0:
                if r - kr < 0:
                    msg = msg + to_hex(r - kr + 256)
                else:
                    msg = msg + to_hex(r - kr)
                c = c + 1
            elif c == 1:
                if g - kg < 0:
                    msg = msg + to_hex(g - kg + 256)
                else:
                    msg = msg + to_hex(g - kg)
                c = c + 1
            else:
                if b - kb < 0:
                    msg = msg + to_hex(b - kb + 256)
                else:
                    msg = msg + to_hex(b - kb)
                c = 0
        return
