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
