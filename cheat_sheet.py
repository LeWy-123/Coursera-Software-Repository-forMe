#  1. Egyszerű TCP kapcsolat HTTP kéréssel
import socket

host = 'example.com'
port = 80

# Socket létrehozása
# AF_INET = IPv4, SOCK_STREAM = TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

# HTTP GET kérés (csak az útvonal, nem teljes URL)
request = (
    "GET / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Connection: close\r\n"
    "\r\n"
)
sock.send(request.encode())

response = b""
while True:
    data = sock.recv(1024)
    if not data:
        break
    response += data

sock.close()

# Tartalom mentése fájlba
with open("response.txt", "wb") as f:
    f.write(response)

#  2. HTTPS kapcsolat (SSL socket)
import socket
import ssl

host = 'www.google.com'
port = 443

context = ssl.create_default_context()
sock = socket.create_connection((host, port))
ssock = context.wrap_socket(sock, server_hostname=host)

request = (
    "GET / HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    "Connection: close\r\n"
    "\r\n"
)
ssock.send(request.encode())

response = b""
while True:
    data = ssock.recv(1024)
    if not data:
        break
    response += data

ssock.close()

# Mentés fájlba
with open("google_https_response.txt", "wb") as f:
    f.write(response)

# 3. Fájl olvasása szövegként
with open("response.txt", "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()
    print(content)

# 4. Fájl írása (szöveges)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Ez egy teszt szöveg.")

#  5. Fájl hozzáfűzés (append mód)
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("\nÚj sor hozzáfűzve.")

import xml.etree.ElementTree as ET

tree = ET.fromstring(xml_string)

# 3. XML feldolgozás ElementTree modullal
#✅ Alapvető XML parsing
# Példa: bejárás
for item in tree.findall(".//item"):
    title = item.find("title").text
    link = item.find("link").text
    print("Cím:", title)
    print("Link:", link)
