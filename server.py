import socket
import threading

def start_server(port, banner):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    print(f"[+] Listening on port {port}")

    while True:
        client, addr = server.accept()
        client.send(banner.encode())
        client.close()

services = {
    21: "FTP Service\n",
    22: "SSH Service\n",
    80: "HTTP Service\n",
    443: "HTTPS Service\n"
}

for port, banner in services.items():
    threading.Thread(target=start_server, args=(port, banner)).start()