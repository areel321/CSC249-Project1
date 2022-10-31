#import socket
from socket import *
#import sys to accept command line arguments
import sys

#fill variables from command line
#server_host = sys.argv[1]
#server_port = sys.argv[2]
#filename = sys.argv[3]

#hardcoded variables
server_host = '131.229.198.171'
server_port = 1024
filename = 'HelloWorld.html'

#set up client socket and connect to server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server_host, server_port))

try:
    #send HTML file to socket
    clientSocket.sendall(f'GET /{filename}\nContent-Type: text/html\n\n'.encode())
    message = clientSocket.recv(4096)
    data = message.decode()

    print('recieved')

#handle errors
except IOError:
    print('error')

