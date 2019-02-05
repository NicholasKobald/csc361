from __future__ import print_function
import socket
import sys 



def main(path, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                 

    s.connect(("", 80))

    s.sendall("GET {} HTTP/1.1\n\n".format(path))

    all_responses = [] 
    while True:
        chunk = s.recv(4096) 
        if chunk == b'':
            break 
        else:
            all_responses.append(chunk)

    print(''.join(all_responses))


if  __name__ == "__main__":
    try:
        main(sys.argv[1], int(sys.argv[2]))
    except:
        print("Usage: python client.py path port_no")