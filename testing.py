import time
from Steganography import encode, decode
from PIL import Image


def test_encode_speed():
    start = time.time()
    nonce, tag = encode('pfp.png',
                        'mngvo4wbROWpQYdy3vedGx9TS!Zc$BpCUpRju#Z$txhVsP1%*0orgg0sY660Tw6x!jDOJgZBGc9edqzBYJSmXHGAhd9*BhzDR@cD',
                        '02b63d517eaeb1127f2aa4eaf82a2a8a53f6c73674ec674696cf1686fb10d368')
    end = time.time()
    total = end - start
    start = time.time()
    nonce, tag = encode('pfp.png',
                        'hMDpNgB3RJX%tr+vnoO$oOg@D4Ox3QDyOjtJcU&anQ@16PSS@qQG0!tpwrOz$suRJo1zDDG9u@0ArE!JBG#Cb7&edC*W5nBz7drT',
                        'cd30fce4a533974b933752c23f1f605fe3c6eaba2a9d6c09e7b1be4f675b5cab')
    end = time.time()
    total = total + (end - start)
    start = time.time()
    nonce, tag = encode('pfp.png',
                        '#d865x0WFjCvHe0MxOd%MVe1zX$B7RvVk=poJgE3%te#C6+Ah@mJ6gg9qOJROAD+KbodMY+u#%aEon!wrnRfn!0V9t0s0J3+$tt5',
                        '05481d5feea6b89db00ccb24f6cfaf6ea285ea21724b8b29b4d7482a9eb74bff')
    end = time.time()
    total = total + (end - start)
    start = time.time()
    nonce, tag = encode('pfp.png',
                        'aw7yu#vdNHO3qGmWJAhVqMPhYTryYuZDKSbDAH223OrHtU6@JJ@aCq@w4d9+XuSy&!1X#q!S9$mZnuu#OgOR1XdZ2M4XY@$z5D*=',
                        '9d149559c249bf12a6f5a605d97d0bbd31f89db27a2105e8622a5c0a5e8d9a62')
    end = time.time()
    total = total + (end - start)
    start = time.time()
    nonce, tag = encode('pfp.png',
                        'ScpsUwtBpQw7$@!Uredtv1DP=@!@z4w!*EPoNXWNMhvJWg1*JCSdddZc8phBohaBnG#2hqbKOnDqTNJSMU#pe9O8q+YqzxZ6C&q8',
                        '2a2b4e3337d863c8903447a55673fa00cbb3b27f25fa7fb824975ea2fd875fd1')
    end = time.time()
    total = total + (end - start)
    mean = total / 5
    return mean


def test_decode_speed():
    nonce, tag = encode('pfp.png',
                        'mngvo4wbROWpQYdy3vedGx9TS!Zc$BpCUpRju#Z$txhVsP1%*0orgg0sY660Tw6x!jDOJgZBGc9edqzBYJSmXHGAhd9*BhzDR@cD',
                        '02b63d517eaeb1127f2aa4eaf82a2a8a53f6c73674ec674696cf1686fb10d368')
    start = time.time()
    decode('encoded.png', nonce, tag, '02b63d517eaeb1127f2aa4eaf82a2a8a53f6c73674ec674696cf1686fb10d368')
    end = time.time()
    total = end - start
    nonce, tag = encode('pfp.png',
                        'hMDpNgB3RJX%tr+vnoO$oOg@D4Ox3QDyOjtJcU&anQ@16PSS@qQG0!tpwrOz$suRJo1zDDG9u@0ArE!JBG#Cb7&edC*W5nBz7drT',
                        'cd30fce4a533974b933752c23f1f605fe3c6eaba2a9d6c09e7b1be4f675b5cab')
    start = time.time()
    decode('encoded.png', nonce, tag, 'cd30fce4a533974b933752c23f1f605fe3c6eaba2a9d6c09e7b1be4f675b5cab')
    end = time.time()
    total = total + (end - start)
    nonce, tag = encode('pfp.png',
                        '#d865x0WFjCvHe0MxOd%MVe1zX$B7RvVk=poJgE3%te#C6+Ah@mJ6gg9qOJROAD+KbodMY+u#%aEon!wrnRfn!0V9t0s0J3+$tt5',
                        '05481d5feea6b89db00ccb24f6cfaf6ea285ea21724b8b29b4d7482a9eb74bff')
    start = time.time()
    decode('encoded.png', nonce, tag, '05481d5feea6b89db00ccb24f6cfaf6ea285ea21724b8b29b4d7482a9eb74bff')
    end = time.time()
    total = total + (end - start)
    nonce, tag = encode('pfp.png',
                        'aw7yu#vdNHO3qGmWJAhVqMPhYTryYuZDKSbDAH223OrHtU6@JJ@aCq@w4d9+XuSy&!1X#q!S9$mZnuu#OgOR1XdZ2M4XY@$z5D*=',
                        '9d149559c249bf12a6f5a605d97d0bbd31f89db27a2105e8622a5c0a5e8d9a62')
    start = time.time()
    decode('encoded.png', nonce, tag, '9d149559c249bf12a6f5a605d97d0bbd31f89db27a2105e8622a5c0a5e8d9a62')
    end = time.time()
    total = total + (end - start)
    nonce, tag = encode('pfp.png',
                        'ScpsUwtBpQw7$@!Uredtv1DP=@!@z4w!*EPoNXWNMhvJWg1*JCSdddZc8phBohaBnG#2hqbKOnDqTNJSMU#pe9O8q+YqzxZ6C&q8',
                        '2a2b4e3337d863c8903447a55673fa00cbb3b27f25fa7fb824975ea2fd875fd1')
    start = time.time()
    decode('encoded.png', nonce, tag, '2a2b4e3337d863c8903447a55673fa00cbb3b27f25fa7fb824975ea2fd875fd1')
    end = time.time()
    total = total + (end - start)
    mean = total / 5
    return mean


def speed_test():
    average = test_encode_speed()
    for x in range(0, 98):
        temp = test_encode_speed()
        average = average + temp
    averageMean = average / 100
    print(averageMean)
