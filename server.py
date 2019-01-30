from __future__ import print_function
# import socket # module
import socket  
import sys # In order to terminate the program

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Prepare a server socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print("host name is", socket.gethostname())
print('running on port 80')
serversocket.bind((socket.gethostname(), 80))
serversocket.listen(5)

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
        
        connectionSock
        
        et.close()
    except IOError:
        pass
        # Send response message for file not found
        # ????????????
        # Close client socket

serverSocket.close()
sys.exit()
