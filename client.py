import tkinter as tk
from tkinter import ttk, filedialog
import socket
import threading
import time
import csv
from concurrent.futures import ThreadPoolExecutor

# ----------------  SERVER IP ---------------- #
DEFAULT_IP = "10.150.154.173"  

# ---------------- SERVICE MAP ---------------- #
services_map = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}

results = []
completed_ports = 0
is_scanning = False

# ---------------- SCANNER ---------------- #
def scan_ports(target, start_port, end_port):
    global completed_ports, is_scanning

    is_scanning = True
    export_button.config(state="disabled")

    output_box.delete("1.0", tk.END)
    status_label.config(text=f"🔍 Scanning {target}...", fg="cyan")

    total_ports = end_port - start_port + 1
    progress["maximum"] = total_ports
    progress["value"] = 0
    completed_ports = 0
    results.clear()

    start_time = time.time()

    def update_progress():
        global completed_ports
        completed_ports += 1
        progress["value"] = completed_ports
        percent = int((completed_ports / total_ports) * 100)
        progress_label.config(text=f"{percent}%")

    def scan_port(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)

            if s.connect_ex((target, port)) == 0:
                try:
                    banner = s.recv(1024).decode().strip()
                except:
                    banner = "Unknown"

                service = services_map.get(port, "Unknown")

                root.after(0, lambda: results.append((port, service, banner)))

                output_box.insert(
                    tk.END,
                    f"[OPEN] Port {port} | {service} | {banner}\n",
                    "open"
                )

            s.close()
        except:
            pass

        root.after(0, update_progress)

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_port, range(start_port, end_port + 1))

    end_time = time.time()

    progress["value"] = total_ports
    progress_label.config(text="100%")

    output_box.insert(
        tk.END,
        f"\n✅ Completed in {end_time - start_time:.2f} seconds\n"
    )

    status_label.config(text="✔ Scan Completed", fg="lime")

    is_scanning = False
    export_button.config(state="normal")


# ---------------- BUTTON FUNCTIONS ---------------- #
def start_scan():
    try:
        # 🔥 USE DEFAULT IP IF EMPTY
        target = entry_ip.get().strip() or DEFAULT_IP

        start_port = int(entry_start.get())
        end_port = int(entry_end.get())

        threading.Thread(
            target=scan_ports,
            args=(target, start_port, end_port)
        ).start()

    except:
        status_label.config(text="❌ Invalid Input", fg="red")


def export_csv():
    if is_scanning:
        status_label.config(text="⚠ Wait for scan to finish", fg="orange")
        return

    if not results:
        status_label.config(text="⚠ No data to export", fg="orange")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")]
    )

    if file_path:
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Port", "Service", "Banner"])
            writer.writerows(results)

        status_label.config(text="📁 Exported Successfully", fg="green")


# ---------------- UI ---------------- #
root = tk.Tk()
root.title("TCP Port Scanner")
root.geometry("700x600")
root.configure(bg="#0f172a")

main = tk.Frame(root, bg="#0f172a")
main.pack(pady=10)

tk.Label(main, text="🚀 TCP PORT SCANNER",
         font=("Arial", 18, "bold"),
         bg="#0f172a", fg="cyan").pack(pady=10)

def create_input(label):
    frame = tk.Frame(main, bg="#0f172a")
    frame.pack(pady=5)

    tk.Label(frame, text=label, width=12,
             bg="#0f172a", fg="white").pack(side="left")

    entry = tk.Entry(frame, width=25)
    entry.pack(side="left")

    return entry

entry_ip = create_input("Target IP")
entry_ip.insert(0, DEFAULT_IP)   # 🔥 AUTO-FILL

entry_start = create_input("Start Port")
entry_end = create_input("End Port")

btn_frame = tk.Frame(main, bg="#0f172a")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Start Scan",
          command=start_scan,
          bg="green", fg="white").grid(row=0, column=0, padx=10)

export_button = tk.Button(btn_frame, text="Export CSV",
                          command=export_csv,
                          bg="yellow")
export_button.grid(row=0, column=1, padx=10)

progress = ttk.Progressbar(main, length=400)
progress.pack(pady=10)

progress_label = tk.Label(main, text="0%",
                          bg="#0f172a", fg="white")
progress_label.pack()

status_label = tk.Label(main, text="Idle",
                        bg="#0f172a", fg="white")
status_label.pack()

output_box = tk.Text(main, height=15, width=80,
                     bg="black", fg="lime")
output_box.pack()

output_box.tag_config("open", foreground="lime")

root.mainloop()
