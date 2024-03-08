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
    x = 0
    y = 0
    for char in msg:
        if x >= height:
            y = y + 1
            x = 0
        pix[x, y] = ord(char), ord(char), ord(char), 255
        print(char)
        print(pix[x, y])
        print('X:', x, 'Y:', y)
        x = x + 1
    im.save('test.png')
    return


def decode(encoded):
    msg = ""
    return msg


encode('pfp.png',
       'What the fuck did you just fucking say about me, you little shit? Ill have you know I graduated top of my class in the Navy Seals, and Ive been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and Im the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. Youre fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and thats just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little clever comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldnt, you didnt, and now youre paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. Youre fucking dead, kiddo. ')
