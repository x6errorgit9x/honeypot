import socket
from datetime import datetime

from database import save_attack
from mitre_mapper import map_attack

HOST = "0.0.0.0"
PORT = 2222

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"[+] Fake SSH Honeypot listening on {PORT}")

while True:
    client, addr = server.accept()
    ip = addr[0]

    try:
        client.send(b"SSH-2.0-OpenSSH_8.2\r\n")
        client.send(b"login: ")
        username = client.recv(1024).decode().strip()

        client.send(b"password: ")
        password = client.recv(1024).decode().strip()

        technique = map_attack(ip, username, password)

        save_attack(
            ip,
            username,
            password,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            technique
        )

        client.send(b"Permission denied\r\n")
    except Exception as e:
        print(e)

    client.close()
