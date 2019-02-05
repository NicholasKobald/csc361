from __future__ import print_function
# import socket # module
import socket  
import sys # In order to terminate the program

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Prepare a server socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print("host name is", socket.gethostname())
print('running on port 9999')
serversocket.bind(('', 9999))
serversocket.listen(1)
#
# 
# command to start things up: sudo mn -x 
# TELUS payment services: 
# 1-800-777-1888 
# 
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serversocket.accept()  
            
    try:
        message = connectionSocket.recv(1024)
        print('received message is:')
        print(message)            
        filename = message.split()[1] 
        print('parsed filename as:', filename)                
        with open(filename[1:]) as f:
            outputdata = f.read()

        print('going to send output data:', outputdata)              
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.0 200 OK\r\n')
        print('sent 200 ok')
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        # Send HTTP response message for file not found
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
		connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
        connectionSocket.close() 
        # Send response message for file not found
        # ????????????
        # Close client socket

serverSocket.close()
sys.exit()
