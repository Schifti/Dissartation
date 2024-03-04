import aes

key = 'Test'


def encode(image, msg):

    encoded = ''
    return encoded


def decode(encoded):
    msg = ""
    return msg


# Test
print(encode('image', 'Hello World'))

# example of using mode of operation
mk = 0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
mk_arr = aes.utils.int2arr8bit(mk, 32)
pt = 0x00112233445566778899aabbccddeeff
pt_arr = aes.utils.int2arr8bit(pt, 16)


cipher = aes.aes(mk, 256, mode='CTR', padding='PKCS#7')

# notice: enc/dec can only 'list'  !!
ct_arr = cipher.enc(pt_arr)
print("0x"+hex(aes.utils.arr8bit2int(ct_arr))[2:].zfill(32))

pr_arr = cipher.dec(ct_arr)
print("0x"+hex(aes.utils.arr8bit2int(pr_arr))[2:].zfill(32))

