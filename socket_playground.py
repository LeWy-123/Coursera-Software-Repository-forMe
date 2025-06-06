import socket
import ssl

URL = input("Enter URL: ")

hostname = URL
port = 443  # HTTPS

context = ssl.create_default_context()
sock = socket.create_connection((hostname, port))
ssock = context.wrap_socket(sock, server_hostname=hostname)

request = (
    "GET / HTTP/1.1\r\n"
    f"Host: {hostname}\r\n"
    "Connection: close\r\n"
    "\r\n"
)
ssock.send(request.encode())

all_data = b''

while True:
    data = ssock.recv(1024)
    if not data:
        break
    print(data.decode(errors="ignore"))
    all_data += data

ssock.close()

print('------------- connection closed -------------')
pos = all_data.decode(errors="ignore").find('\r\n\r\n')
print(all_data.decode(errors="ignore")[pos+4:])