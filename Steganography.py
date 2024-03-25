from PIL import Image
import random


def encode(image, msg, seed):
    im = Image.open(image)
    pix = im.load()
    width, height = im.size
    c = 0
    coords = []
    random.seed(seed)
    for char in msg:
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
        if c == 0:
            if r + ord(char) > 255:
                pix[x, y] = r + ord(char) - 256, g, b, o
            else:
                pix[x, y] = r + ord(char), g, b, o
            c = c + 1
        elif c == 1:
            if g + ord(char) > 255:
                pix[x, y] = r, g + ord(char) - 256, b, o
            else:
                pix[x, y] = r, g + ord(char), b, o
            c = c + 1
        elif c == 2:
            if b + ord(char) > 255:
                pix[x, y] = r, g, b + ord(char) - 256, o
            else:
                pix[x, y] = r, g, b + ord(char), o
            c = 0
    pix[random.randint(0, width - 2), random.randint(0, height - 2)] = 0, 255, 174, 255
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
        x, y = random.randint(0, width - 2), random.randint(0, height - 2)
        r, g, b, o = pix[x, y]
        if pix[x, y] == (0, 255, 174, 255):
            return msg
        kr, kg, kb, ko = pix[x + 1, y]
        if o == 254:
            o = 255
        elif c == 0:
            if r - kr < 0:
                msg = msg + chr(r - kr + 256)
            else:
                msg = msg + chr(r - kr)
            c = c + 1
        elif c == 1:
            if g - kg < 0:
                msg = msg + chr(g - kg + 256)
            else:
                msg = msg + chr(g - kg)
            c = c + 1
        else:
            if b - kb < 0:
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


key = 1234567890
msg = ("The US has filed a landmark lawsuit against Apple which accuses the tech giant of monopolising the smartphone "
       "market and crushing competition. In the lawsuit, the justice department alleges the company used its control "
       "of the iPhone to illegally limit competitors and consumer options.")

encode('pfp.png', msg, key)
ans = decode('test.png', key)
count = 0
yes = 0
no = 0
for char in ans:
    if char == msg[count]:
        yes = yes + 1
    else:
        no = no + 1
    count = count + 1
if msg == ans:
    print('Match')
else:
    print('No match', (yes / len(msg)) * 100, '% Correct', no, 'Incorrect')
    print(ans)
