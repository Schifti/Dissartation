from Crypto.Cipher import AES
import secrets


def key_gen():
    key = secrets.token_hex(32)
    return key


def encrypt(msg, key):
    cipher = AES.new(bytearray.fromhex(key), AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('utf-8'))
    return nonce.hex(), ciphertext.hex(), tag.hex()


def decrypt(nonce, ciphertext, tag, key):
    cipher = AES.new(bytearray.fromhex(key), AES.MODE_EAX, nonce=bytearray.fromhex(nonce))
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(bytearray.fromhex(tag))
        return plaintext.decode('utf-8')
    except:
        return False
