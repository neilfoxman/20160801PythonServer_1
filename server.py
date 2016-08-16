# http://www.binarytides.com/python-socket-programming-tutorial/

import socket
import sys

HOST = '' # symbolic name meaning all available interfaces
PORT = 8888 # Set port no

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create TCP Socket
print("Socket created")

try:
    s.bind((HOST, PORT)) # Bind to port
except socket.error as msg:
    print("Bind failed. Error code: "+str(msg[0])+". Message: "+msg[1])
    sys.exit()
print("Socket bind complete")

s.listen(10) # Listen for a client (backlog up to 10 connections)
print("Socket now listening")

conn, addr = s.accept() # Accept connection, returns new socket connection and address of other end
print("Connected with IP:"+addr[0]+" at client port:"+str(addr[1]))
conn.send(b"yo\n\r")
print("Yo sent")

data = "doof"
while data != "q":
    data = conn.recv(1024).decode("utf-8")
    print("Before data printed")
    print(data)
    print("After data printed")
    if not data:
        print("Connection closed by client")
        break

conn.close()
s.close()


