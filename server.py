import socket
import threading

services = {
    21: b"FTP Server Ready\r\n",
    22: b"SSH-2.0-OpenSSH_7.4\r\n",
    80: b"HTTP/1.1 200 OK\r\nServer: Apache\r\n\r\n",
    443: b"HTTPS Service Ready\r\n"
}

def handle_client(conn, addr, banner):
    try:
        conn.send(banner)
    except:
        pass
    conn.close()

def start_server(port, banner):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    print(f"[+] Listening on port {port}")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr, banner)).start()

for port, banner in services.items():
    threading.Thread(target=start_server, args=(port, banner)).start()
