import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.google.fr", 80))
s.send('GET /index.php HTTP/1.1\r\n\r\n')
while 1:
    data = s.recv(128)
    print data
    if data == "":
        break
s.close()

