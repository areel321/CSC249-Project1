__author__ = "Allison Reel"
# I consulted https://docs.python.org/3/library/socket.html and https://docs.python.org/3/howto/sockets.html on how to use sockets and socket funtions.  
# I also used https://www.w3schools.com/html/html_editors.asp and https://www.w3schools.com/html/html_styles.asp on how to create and read my HTML file.  
# I worked with my classmates Hamssatou Maiga, Larissa Savitsky, and Paola Calle to discuss our programs

from socket import *
import sys # In order to terminate the program
import threading # import for multithreaded server
from _thread import *




serverSocket = socket(AF_INET, SOCK_STREAM)

# -------------
# Fill in start
# -------------

  # TODO: Assign a port number
  
  #       Bind the socket to server address and server port
  #       Tell the socket to listen to at most 1 connection at a time
  # binded to my computer's ip address, and I read in the documentation that ports above 1023 are non-privledged 
serverSocket.bind(('', 1024))
# listen to only one connection
serverSocket.listen(1)
# -----------
# Fill in end
# -----------
LMAO = 0
while True:
    
    # Establish the connection
    print('Ready to serve...') 
    
    # -------------
    # Fill in start
    # -------------
    connectionSocket, addr = serverSocket.accept() # TODO: Set up a new connection from the client
    # -----------
    # Fill in end
    # -----------
    # 
    print_lock = threading.Lock()
    def multiThread(connectionSocket):
        while True:
            message = connectionSocket.recv(4096)
            if not message:
                break
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n'.encode())
            for i in range(0, len(outputdata)):
             connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    try:
        print_lock.acquire()
        print("connected")
        start_new_thread(multiThread, (connectionSocket,))
        LMAO+=1
        print(LMAO)
        # -------------
        # Fill in start
        # -------------
        # the socket documentation recommended using a power of two in recv
        ##message = connectionSocket.recv(4096) # TODO: Receive the request message from the client
        # -----------
        # Fill in end
        # -----------
        
        # Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]

        ##filename = message.split()[1]


        # Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character
        ##f = open(filename[1:])
        
        # -------------
        # Fill in start
        # -------------
        ##outputdata = f.read() # TODO: Store the entire contents of the requested file in a temporary buffer
        # -----------
        # Fill in end
        # -----------

        # -------------
        # Fill in start
        # -------------
        # have to encode str to convert to bytes
        # I used https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml to get the correct response message
        ##connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n'.encode())    # TODO: Send one HTTP header line into socket
        # -----------
        # Fill in end
        # -----------

        # Send the content of the requested file to the client
        ##for i in range(0, len(outputdata)):
          ##  connectionSocket.send(outputdata[i].encode())
        ##connectionSocket.send("\r\n".encode())

        ##connectionSocket.close()

    except IOError:
        # -------------
        # Fill in start
        # -------------
            # TODO: Send response message for file not found
            #       Close client socket
            connectionSocket.send('HTTP/1.1 404 Not Found'.encode()) 
            connectionSocket.close()
        # -----------
        # Fill in end
        # -----------

serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data