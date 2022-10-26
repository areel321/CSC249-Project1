
# i consulted the python HTTP documentation on how to create a client-side of a server here https://docs.python.org/3/library/http.client.html
import http.client
import sys


#server_host = sys.argv[1:16]
#server_port = sys.argv[17:20]
#filename = sys.argv[21:]
server_host = ''
server_port = 1024
filename = 'HelloWorld.html'

#add / to the beginning of the filename
filename = str('/'+filename)
#start the HTTP connection
conn = http.client.HTTPConnection(str(server_host), server_port)
#use get request
conn.request("GET", filename)
#recieve and read contents of the server
response = conn.getresponse()
data = response.read()

