import socket
import threading
import time
from queue import Queue

class PortScannerClient:
    def __init__(self, target, start_port, end_port, threads=50):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.threads = threads

        self.queue = Queue()
        self.open_ports = []
        self.lock = threading.Lock()

    def scan_port(self, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)

            result = s.connect_ex((self.target, port))

            if result == 0:
                try:
                    banner = s.recv(1024).decode().strip()
                except:
                    banner = "No banner"

                with self.lock:
                    self.open_ports.append((port, banner))

            s.close()
        except:
            pass

    def worker(self):
        while not self.queue.empty():
            port = self.queue.get()
            self.scan_port(port)
            self.queue.task_done()

    def run_scan(self):
        start_time = time.time()

        for port in range(self.start_port, self.end_port + 1):
            self.queue.put(port)

        threads = []
        for _ in range(self.threads):
            t = threading.Thread(target=self.worker)
            t.start()
            threads.append(t)

        self.queue.join()

        end_time = time.time()

        return self.open_ports, end_time - start_time