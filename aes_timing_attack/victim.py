# victim.py
from aes_tables import aes_encrypt
import numpy as np

key = [0x42, 0x37, 0x81, 0xFA]
def victim_encrypt(plaintext):
    return aes_encrypt(plaintext, key)
