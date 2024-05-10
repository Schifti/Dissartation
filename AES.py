from Crypto.Cipher import AES

key = b'Sixteen byte key'


def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('utf-8'))
    return nonce, ciphertext, tag


def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('utf-8')
    except:
        return False


'''msg = (
    "The US has filed a landmark lawsuit against Apple which accuses the tech giant of monopolising the smartphone "
    "market and crushing competition. In the lawsuit, the justice department alleges the company used its control "
    "of the iPhone to illegally limit competitors and consumer options.")
nonce, ciphertext, tag = encrypt(msg)
print(ciphertext)
hexxed = ciphertext.hex()
print('hexxed:', hexxed, len(hexxed))
unhex = bytes.fromhex(hexxed)
if unhex == ciphertext:
    print('hexy works')
print(decrypt(nonce, unhex, tag), len(msg))'''
