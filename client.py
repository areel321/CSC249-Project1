"""
import http.client
import sys

server_host = sys.argv[1:]
server_port = sys.argv[2]
filename = sys.argv[3]
#filename = 'HelloWorld.html'
print(filename)

#def client(server_host, server_port, filename):
filename = str('/'+filename)
conn = http.client.HTTPConnection(str(server_host), server_port)
conn.request("GET", filename)
response = conn.getresponse()
data = response.read()

#client(server_host, server_port, filename)
"""

from socket import *
import sys
#server_host = sys.argv[1:]
#server_port = sys.argv[2]
#filename = sys.argv[3]
server_host = '131.229.198.171'
server_port = 1024
filename = 'HelloWorld.html'

def client(server_host, server_port, filename):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((str(server_host), server_port))
    client_socket.send(filename.encode())
    client_socket.recv(server_port).decode()
    client_socket.close()

client(server_host, server_port, filename)
