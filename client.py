from __future__ import print_function
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                 

s.connect(("nicholas-ThinkPad-X1-Yoga-1st", 80))

s.sendall("GET /test-file-name.txt HTTP/1.1\n\n")

all_responses = [] 
while True:
    chunk = s.recv(4096) 
    if chunk == b'':
        break 
    else:
        all_responses.append(chunk)

print(''.join(all_responses))