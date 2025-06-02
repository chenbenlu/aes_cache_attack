import subprocess
import re
import matplotlib.pyplot as plt

def run_aes_demo():
    result = subprocess.run(["./aes_demo"], capture_output=True, text=True)
    output = result.stdout
    match = re.search(r"Access time to sbox\[0x63\] after flush: (\d+) cycles", output)
    if match:
        return int(match.group(1))
    return None

def collect_timings(samples=100):
    timings = []
    for _ in range(samples):
        cycles = run_aes_demo()
        if cycles is not None:
            timings.append(cycles)
    return timings

def plot_timings(timings):
    plt.figure(figsize=(10, 4))
    plt.plot(timings, marker='o', linestyle='-', label='Access Time')
    plt.axhline(y=sum(timings) / len(timings), color='r', linestyle='--', label='Average')
    plt.title("Timing Access to sbox[0x63] After Flush")
    plt.xlabel("Sample")
    plt.ylabel("Cycles")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Collecting timing samples...")
    timings = collect_timings(100)
    plot_timings(timings)
