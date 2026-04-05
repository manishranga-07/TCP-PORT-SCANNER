import tkinter as tk
from tkinter import messagebox
from client import PortScannerClient
import threading

def start_scan():
    target = entry_target.get()
    try:
        start_port = int(entry_start.get())
        end_port = int(entry_end.get())
    except:
        messagebox.showerror("Error", "Invalid port numbers")
        return

    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, "Scanning...\n")

    def run():
        scanner = PortScannerClient(target, start_port, end_port)
        results, duration = scanner.run_scan()

        result_box.insert(tk.END, f"\nScan completed in {duration:.2f}s\n\n")

        for port, banner in sorted(results):
            result_box.insert(tk.END, f"Port {port} OPEN | {banner}\n")

    threading.Thread(target=run).start()


# UI Window
root = tk.Tk()
root.title("TCP Port Scanner")
root.geometry("500x400")

# Input fields
tk.Label(root, text="Target IP").pack()
entry_target = tk.Entry(root)
entry_target.pack()

tk.Label(root, text="Start Port").pack()
entry_start = tk.Entry(root)
entry_start.pack()

tk.Label(root, text="End Port").pack()
entry_end = tk.Entry(root)
entry_end.pack()

# Button
tk.Button(root, text="Start Scan", command=start_scan).pack(pady=10)

# Output box
result_box = tk.Text(root, height=15)
result_box.pack()

root.mainloop()
