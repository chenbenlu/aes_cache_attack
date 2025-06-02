import subprocess
import time

def measure(m, trials=5):
    total = 0
    for _ in range(trials):
        start = time.perf_counter_ns()
        subprocess.run(["./victim", str(m)], stdout=subprocess.DEVNULL)
        end = time.perf_counter_ns()
        total += end - start
    return total // trials

if __name__ == "__main__":
    for m in range(2, 100):
        t = measure(m)
        print(f"{m},{t}")
