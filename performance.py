import matplotlib.pyplot as plt
import subprocess
import time

thread_counts = [10, 50, 100, 200]
times = []

for threads in thread_counts:
    start = time.time()

    subprocess.run(["python", "scanner.py"], input=b"127.0.0.1\n1\n1000\n")

    end = time.time()
    times.append(end - start)

plt.plot(thread_counts, times)
plt.xlabel("Number of Threads")
plt.ylabel("Time Taken (seconds)")
plt.title("Scan Efficiency vs Threads")
plt.show()