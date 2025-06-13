import socket
import ssl

HOST = 'www.edmeeatrans.ro'
PORT = 443

# SSL context to ignore cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Raw socket wrapped in SSL
raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ctx.wrap_socket(raw_sock, server_hostname=HOST)

# Connect to server
ssl_sock.connect((HOST, PORT))

# Proper GET request with User-Agent and blank line at the end
request = (
    'GET / HTTP/1.1\r\n'
    f'Host: {HOST}\r\n'
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/114.0.0.0 Safari/537.36\r\n'
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n'
    'Connection: close'
    'Accept-Language: en-US,en;q=0.5\r\n'
    '\r\n'
)

# Send the request
ssl_sock.send(request.encode())

# Receive and decode the response
response = b""
while True:
    data = ssl_sock.recv(1024)
    if not data:
        break
    response += data

print(response.decode(errors='ignore'))

# Close connection
ssl_sock.close()
