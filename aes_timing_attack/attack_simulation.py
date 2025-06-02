import numpy as np
import matplotlib.pyplot as plt
import time

# 固定 AES key（模擬用）
key = [0x42, 0x37, 0x81, 0xFA]

# 模擬的 T-table（類似 AES 的查表）
np.random.seed(0)
SBOX = np.random.permutation(256)
T_TABLE = np.array([[SBOX[(i + r) % 256] for i in range(256)] for r in range(4)])

# 模擬 AES encryption
def aes_encrypt(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        k = key[i % len(key)]
        byte = plaintext[i]
        result = T_TABLE[i % 4][byte ^ k]
        ciphertext.append(result)
    return ciphertext

# 模擬 flush cache 的動作（實際上使用大量資料來逼 cache reload）
def flush_cache():
    dummy = np.zeros((1024 * 1024,), dtype=np.uint8)
    dummy[np.random.randint(0, len(dummy), size=1000)] = 1

# 測量某 byte 輸入值的平均加密時間
def measure_byte_timing(byte_val, key_byte_pos, trials=1000):
    timings = []
    plaintext = [0] * 16
    for _ in range(trials):
        flush_cache()
        plaintext[key_byte_pos] = byte_val
        start = time.perf_counter_ns()
        _ = aes_encrypt(plaintext, key)
        end = time.perf_counter_ns()
        noise = 0  # 移除隨機噪聲
        timings.append(end - start + noise)
    return np.mean(timings)


# 對某 byte 位置進行攻擊
def attack_byte(key_byte_pos):
    print(f"[+] Attacking key byte position {key_byte_pos}")
    scores = []
    for byte in range(256):
        avg_time = measure_byte_timing(byte, key_byte_pos)
        scores.append(avg_time)
    return scores

# 主函式
def main():
    np.random.seed(0)  # 確保隨機性固定
    key_byte_pos = 0
    scores = attack_byte(key_byte_pos)

    plt.figure(figsize=(12, 6))
    plt.plot(range(256), scores, label=f"Key Byte Position {key_byte_pos}")
    plt.xlabel("Byte Input Value")
    plt.ylabel("Avg Encryption Time (ns)")
    plt.title("Simulated AES Cache Timing Attack")
    plt.grid(True)

    best_guess = np.argmax(scores)
    best_time = scores[best_guess]
    plt.scatter(best_guess, best_time, color='red', s=100, label=f'Best Guess Key Byte: {best_guess}')
    plt.annotate(f'Best Guess: {best_guess}',
                 xy=(best_guess, best_time),
                 xytext=(best_guess+20, best_time+10),
                 arrowprops=dict(facecolor='red', shrink=0.05))

    true_key_byte = key[key_byte_pos]
    true_time = scores[true_key_byte]
    plt.scatter(true_key_byte, true_time, color='green', s=100, label=f'True Key Byte: {true_key_byte}')
    plt.annotate(f'True Key: {true_key_byte}',
                 xy=(true_key_byte, true_time),
                 xytext=(true_key_byte+20, true_time-20),
                 arrowprops=dict(facecolor='green', shrink=0.05))

    plt.legend()
    plt.tight_layout()
    plt.savefig("cache_timing_distribution.png")
    plt.show()

if __name__ == "__main__":
    main()
