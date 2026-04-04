import multiprocessing
import time
import matplotlib.pyplot as plt
from client import PortScannerClient

TARGET = "127.0.0.1"
START_PORT = 1
END_PORT = 500   # keep smaller for testing

def worker(_):
    scanner = PortScannerClient(TARGET, START_PORT, END_PORT)
    _, duration = scanner.run_scan()
    return duration


def run_test(clients):
    print(f"\nRunning with {clients} clients...")

    start = time.time()

    with multiprocessing.Pool(processes=clients) as pool:
        results = pool.map(worker, range(clients))

    total_time = time.time() - start
    avg_time = sum(results) / len(results)

    print(f"Total Time: {total_time:.2f}s")
    print(f"Avg Time per Client: {avg_time:.2f}s")

    return total_time, avg_time


if __name__ == "__main__":   # VERY IMPORTANT (Windows fix)
    client_counts = [1, 2, 4, 8]
    total_times = []
    avg_times = []

    for c in client_counts:
        t, a = run_test(c)
        total_times.append(t)
        avg_times.append(a)

    # -------- GRAPH 1 --------
    plt.figure()
    plt.plot(client_counts, total_times)
    plt.xlabel("Number of Clients")
    plt.ylabel("Total Time (s)")
    plt.title("Load Test - Total Time")
    plt.grid()

    # -------- GRAPH 2 --------
    plt.figure()
    plt.plot(client_counts, avg_times)
    plt.xlabel("Number of Clients")
    plt.ylabel("Avg Time per Client (s)")
    plt.title("Load Test - Avg Time")
    plt.grid()

    plt.show()