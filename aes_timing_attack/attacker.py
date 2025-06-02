# attacker.py
from victim import victim_encrypt
from aes_tables import T_TABLE
import numpy as np
import matplotlib.pyplot as plt
import time

def flush_cache():
    dummy = bytearray(10 * 1024 * 1024)  # 大量記憶體強迫 cache eviction
    for i in range(0, len(dummy), 64):
        dummy[i] = 0

def measure_byte_timing(byte_val, key_byte_pos, trials=1000):
    timings = []
    plaintext = [0] * 16
    for _ in range(trials):
        flush_cache()
        plaintext[key_byte_pos] = byte_val
        start = time.perf_counter_ns()
        _ = victim_encrypt(plaintext)
        end = time.perf_counter_ns()
        timings.append(end - start)
    return np.mean(timings)

def attack_byte(key_byte_pos):
    print(f"[*] Attacking key byte position {key_byte_pos}")
    scores = []
    for byte in range(256):
        avg_time = measure_byte_timing(byte, key_byte_pos)
        scores.append(avg_time)
    return scores

def main():
    key_byte_pos = 0
    scores = attack_byte(key_byte_pos)
    
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 5))
    plt.plot(range(256), scores)
    plt.xlabel("Byte value input to AES")
    plt.ylabel("Average encryption time (ns)")
    plt.title("AES Timing Attack: Byte 0 Position")
    plt.savefig("cache_timing_distribution.png")
    plt.show()

if __name__ == "__main__":
    main()
