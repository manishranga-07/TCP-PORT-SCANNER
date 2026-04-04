# 🔍 Problem Statement: Implement a scanner to detect open ports and services.
#    Project explanation: Concurrent scanning; Timeout & retry logic; Banner grabbing; Scan efficiency evaluation

## 📌 Project Overview

This project is a **TCP-based Port Scanner** developed as part of a Computer Networks project. It detects open ports and running services on a target system using **concurrent scanning**, **banner grabbing**, and **performance evaluation**.

The system follows a **client-server architecture** and includes a **Graphical User Interface (GUI)** for ease of use.

---

## 🚀 Features

* ✅ TCP Port Scanning
* ✅ Multi-threaded concurrent scanning
* ✅ Timeout and retry mechanism
* ✅ Banner grabbing (service detection)
* ✅ GUI interface using Tkinter
* ✅ Load testing using multiprocessing
* ✅ Performance evaluation with graphs

---

## 🧩 Project Structure

```
port_scanner_project/
│
├── server.py          # Simulated server (multiple ports)
├── client.py          # Core scanning logic
├── gui_client.py      # GUI interface
├── load_test.py       # Load testing + graphs
├── performance.py     # analyze the efficiency of the port scanner
└── README.md
```

---

## ⚙️ Technologies Used

* Python
* Socket Programming (TCP)
* Threading (for concurrency)
* Multiprocessing (for load testing)
* Tkinter (GUI)
* Matplotlib (graphs)

---

## ▶️ How to Run

### 1️⃣ Start Server (System 1)

```
python server.py
```

---

### 2️⃣ Run GUI Client (System 2 or same system)

```
python gui_client.py
```

Enter:

* Target IP (e.g., `127.0.0.1` or server IP)
* Start Port (e.g., `1`)
* End Port (e.g., `1000`)

---

### 3️⃣ Run Load Test

```
python load_test.py
```

📊 This will generate:

* Total time vs number of clients graph
* Average scan time graph

---
### 3️⃣ Run Performance 

```
python performance.py
```

📊 This will generate:
* Number of threads vs scan time

---
## 🌐 Running on Two Systems

* Run **server.py** on System 1
* Find IP using `ipconfig`
* Use that IP in GUI client on System 2

Example:

```
Target IP: 192.168.1.x
```

---

## 🔄 Working Principle

1. Client sends TCP connection requests to target ports
2. Server accepts connection (if port open)
3. Server sends a banner message
4. Client reads banner and marks port as open

---

## 📊 Performance Evaluation

* Measures scan time under different loads
* Uses multiprocessing to simulate multiple clients
* Graphs show system efficiency and scalability

---

## 🧪 Load Testing

* Multiple clients run simultaneously
* Measures:

  * Total execution time
  * Average scan time per client

---

## 🧠 Key Concepts

* TCP Socket Programming
* Multi-threading
* Client-Server Model
* Network Scanning Techniques
* Performance Analysis

---

## 🎯 Sample Output

```
Port 21 OPEN | Service: Service running on port 21
Port 80 OPEN | Service: Service running on port 80

Scan completed in 1.25 seconds
```

---

## 🚨 Notes

* Ensure server is running before scanning
* Use correct IP address (not 127.0.0.1 for remote systems)
* Disable firewall if connection is blocked

---

## 📌 Future Enhancements

* UDP scanning
* OS fingerprinting
* Web-based interface
* Real-time progress bar
* Export results to file

---

## 👨‍💻 Authors

* NAME: CHINNALA MANISH RANGA -  SRN : PES2UG24CS135
* NAME: G NIKHIL              -  SRN : PES2UG24CS165

---

## 📜 License

This project is for educational purposes.
