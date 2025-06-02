import pandas as pd
import matplotlib.pyplot as plt

# 讀取 m 和 time 對應關係
data = pd.read_csv("timings.csv", header=None, names=["m", "time"])
data = data.sort_values("m")

# 找出某個 bit 位置是否影響到時間（以 bit 0~7）
def guess_bit(bit_index):
    group_0 = []
    group_1 = []

    for i in range(len(data)):
        m = data.iloc[i]["m"]
        t = data.iloc[i]["time"]
        if (m >> bit_index) & 1:
            group_1.append(t)
        else:
            group_0.append(t)

    if len(group_0) == 0 or len(group_1) == 0:
        print(f"Warning: No data in one group for bit {bit_index}")
        return False  # 或其他預設值，例如 False

    avg0 = sum(group_0) / len(group_0)
    avg1 = sum(group_1) / len(group_1)

    return avg1 > avg0

# 對每個 bit 做推論
recovered_bits = []
for i in reversed(range(8)):  # d=173 是 8-bit
    bit = guess_bit(i)
    recovered_bits.append(int(bit))

# 重建私鑰 d
d = 0
for i, b in enumerate(reversed(recovered_bits)):
    d |= b << i

print(f"Recovered d = {d}")
