
from socket import *
import sys

#server_host = sys.argv[1]
#server_port = sys.argv[2]
#filename = sys.argv[3]
server_host = '131.229.198.171'
server_port = 1024
filename = 'HelloWorld.html'

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server_host, server_port))

try:
    clientSocket.sendall(f'GET /{filename}\nContent-Type: text/html\n\n'.encode())
    message = clientSocket.recv(4096)
    data = message.decode()

    print('recieved')

except IOError:
    print("error")

