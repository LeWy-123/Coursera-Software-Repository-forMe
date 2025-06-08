import socket
import ssl
import re

URL = input("Enter URL: ")
#('https://www.py4e.com/tools/python-data/?PHPSESSID=5ca53ef4cacd101795073ffc33e33795')
clean = re.sub(r'^https?://(www\.)?', '', URL)

if 'http' in URL:
    port = 80
else:
    port = 443
print(clean)

hostname = clean

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
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