import matplotlib.pyplot as plt

with open("cache_times.txt") as f:
    times = [int(line.strip()) for line in f]

plt.hist(times, bins=50, color='skyblue', edgecolor='black')
plt.title("Cache Access Time Distribution")
plt.xlabel("Cycles")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
