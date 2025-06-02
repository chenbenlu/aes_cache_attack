import subprocess
import time
import matplotlib.pyplot as plt
import numpy as np

d_bits = 8  # 私鑰 bit 數（上面 d = 173 是 8 bits）
trials_per_plaintext = 5
plaintext_range = range(2, 100)  # 嘗試不同明文

timing_data = {}

for m in plaintext_range:
    times = []
    for _ in range(trials_per_plaintext):
        start = time.perf_counter_ns()
        subprocess.run(["./rsa_victim", str(m)], stdout=subprocess.DEVNULL)
        end = time.perf_counter_ns()
        times.append(end - start)

    avg_time = sum(times) / len(times)
    timing_data[m] = avg_time

# 繪製時間 vs 明文圖
x = list(timing_data.keys())
y = list(timing_data.values())

plt.scatter(x, y, s=10)
plt.xlabel("Plaintext (m)")
plt.ylabel("Decryption Time (ns)")
plt.title("RSA Timing Attack: Decryption Time vs Plaintext")
plt.grid(True)
plt.show()
