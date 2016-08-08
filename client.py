#http://www.binarytides.com/python-socket-programming-tutorial/

import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print("Failed to create socket. Error code: " + str(msg[0])+ ", Error message : " +msg[1])
    sys.exit()
print("socket created")


host = "www.google.com"
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("Host name could not be resolved. Exiting")
    sys.exit()
print("IP address of " + host + " is " + remote_ip)

port = 80
s.connect((remote_ip, port))
print("Socket connected to " + host+" on ip "+remote_ip)

message = b"GET / HTTP/1.1\r\n\r\n"
try:
    s.sendall(message)
except socket.error:
    print("send failed.")
    sys.exit()
print("Message sent successfully")

reply = s.recv(4096)
print(reply)

s.close()

#https://docs.python.org/2/howto/sockets.html
#https://www.raspberrypi.org/forums/viewtopic.php?t=28584
#http://raspberrypi.stackexchange.com/questions/13425/server-and-client-between-pc-and-raspberry-pi

##import socket
##
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##print (socket.gethostname())
##host = ''# ip of raspberry pi
##port = 12345
##
##
####s.connect((host, port))
####print (s.recv(1024))
##s.close




