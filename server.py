# http://www.binarytides.com/python-socket-programming-tutorial/

import socket
import sys

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print("Bind failed. Error code: "+str(msg[0])+". Message: "+msg[1])
    sys.exit()
print("Socket bind complete")

s.listen(10)
print("Socket now listening")

conn, addr = s.accept()
print("Connected with "+addr[0]+":"+str(addr[1]))
conn.sendall(b"yo\n")
print("Yo sent")

x = 0
while x!=1:
    data = str(conn.recv(1024))
    if data == b'quit':
        x = 1
        print("Should be done. X = "+x)
    print(data)
##conn.sendall(data)

##conn.close()
##s.close()
##print("Connection closed")
