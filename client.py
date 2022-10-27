
from socket import *
import sys

#server_host = sys.argv[1:16]
#server_port = sys.argv[17:20]
#filename = sys.argv[21:]
server_host = '131.229.198.171'
server_port = 1024
filename = b'/HelloWorld.html'

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server_host, server_port))

try:
    clientSocket.sendall(filename)
    data = clientSocket.recv(4096)
    print('recieved')

except IOError:
    print("error")

