#https://docs.python.org/2/howto/sockets.html
#https://www.raspberrypi.org/forums/viewtopic.php?t=28584
#http://raspberrypi.stackexchange.com/questions/13425/server-and-client-between-pc-and-raspberry-pi

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print (socket.gethostname())
host = ''# ip of raspberry pi
port = 12345


##s.connect((host, port))
##print (s.recv(1024))
s.close
