import random

SBOX = [i for i in range(256)]
random.shuffle(SBOX)  # 模擬一個隨機 sbox

T_TABLE = [[(SBOX[(i + r) % 256]) for i in range(256)] for r in range(4)]

def aes_encrypt(plaintext, key):
    # 簡化的 AES，模擬 T-table 查詢
    ciphertext = []
    for i in range(len(plaintext)):
        k = key[i % len(key)]
        byte = plaintext[i]
        result = T_TABLE[i % 4][byte ^ k]
        ciphertext.append(result)
    return ciphertext
